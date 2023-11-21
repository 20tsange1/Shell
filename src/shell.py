import sys
import os
import io
from collections import deque
from antlr4 import *
from commands import *
from io_redirection import *
from antlr.Comp0010ShellLexer import Comp0010ShellLexer
from antlr.Comp0010ShellParser import Comp0010ShellParser
from antlr.Comp0010ShellVisitor import Comp0010ShellVisitor


class UnsafeCommandWrapper(Command):
    def __init__(self, wrapped_command):
        self.wrapped_command = wrapped_command

    def execute(self, args, out):
        try:
            # Execute the wrapped command
            self.wrapped_command.execute(args, out)
        except Exception as e:
            # Catch any exceptions and print them to out
            out.append(f"An exception occurred: {str(e)}\n")
            

class CommandExecutor:
    def __init__(self, unsafe=True):
        self.command_map = {
            "pwd": PwdCommand(),
            "cd": CdCommand(),
            "echo": EchoCommand(),
            "ls": LsCommand(),
            "cat": CatCommand(),
            "head": HeadCommand(),
            "tail": TailCommand(),
            "grep": GrepCommand(),
            "sort": SortCommand(),
            "cut": CutCommand(),
            "find": FindCommand(),
            "uniq": UniqCommand(),
        }
        # add unsafe commands to map
        if unsafe:
            self.add_unsafe_commands()

    def add_unsafe_commands(self):
        unsafe = {}
        for command_name, command in self.command_map.items():
            unsafe[f"_{command_name}"] = UnsafeCommandWrapper(command)
        self.command_map.update(unsafe)
    

# make a visitor class which traverses the tree and builds a list of commands

class Visitor(ParseTreeVisitor):

    def __init__(self):
        self.command_list = deque([])
        self.temporary_command = deque([])
        self.temporary_quote = deque([])
        self.output = deque([])
        self.pipe = deque([])
        self.inputIO = InputRedirection()
        self.outputIO = OutputRedirection()

    def visitCommand(self, ctx:Comp0010ShellParser.CommandContext):
        self.visitChildren(ctx)


    # Visit a parse tree produced by Comp0010ShellParser#call.
    def visitCall(self, ctx:Comp0010ShellParser.CallContext):
        self.command_list.append([])
        for i in ctx.getChildren():
            if i.getChild(0):
                if i.getChild(0).getChild(0):
                    if i.getChild(0).getChild(0).getText() == ">":
                        continue
            self.visit(i)
        self.output.append([])
        # print(self.output, 1)
        # print(self.command_list, 2)
        # print(self.temporary_command, 3)
        # print(self.temporary_quote, 4)
        # Check for whether there is a pipe or not, need to change to use stdin
        self.execute_commands(self.command_list[-1], self.output[-1])
        self.command_list.pop()
        for i in ctx.getChildren():
            if i.getChild(0):
                if i.getChild(0).getChild(0):
                    if i.getChild(0).getChild(0).getText() == ">":
                        self.visit(i)
                    if i.getChild(0).getChild(0).getText() == "<":
                        self.inputIO.restore()
                if i.getChild(0).getText() == "<":
                    self.inputIO.restore()
        # print(self.output, 5)
        # print(self.command_list, 6)
        # print(self.temporary_command, 7)
        # print(self.temporary_quote, 8)
        return 

    def visitPipe(self, ctx:Comp0010ShellParser.PipeContext):
        # Reintroducing previous call's arguments -- Change to taking stdout from previous
        with open(".temporary.txt", "w") as pipe:
            self.visit(ctx.getChild(0))
            pipe.write(''.join(self.output.pop()))
        
        inputIO = InputRedirection(".temporary.txt")
        inputIO.redirect_input()

        self.visit(ctx.getChild(2))
        
        inputIO.restore()


    def visitRedirection(self, ctx:Comp0010ShellParser.RedirectionContext):
        index = 2
        if ctx.getChildCount() == 2:
            index = 1
        if ctx.getChild(0).getText() == "<":
            self.inputIO.input_file = ctx.getChild(index).getChild(0).getText()
            self.inputIO.redirect_input()
            # self.inputIO.restore()
        elif ctx.getChild(0).getText() == ">":
            self.outputIO.output_file = ctx.getChild(index).getChild(0).getText()
            self.outputIO.redirect_output("".join(self.output.pop()))
            # outputIO.restore()

        

    def visitArgument(self, ctx:Comp0010ShellParser.ArgumentContext):
        for child in ctx.getChildren():
            if child.getChild(0):
                for child2 in child.getChildren():
                    if child2.__class__.__name__ == "BackquoteContext":
                        self.command_list[-1].append("CMD")
                    else:
                        self.command_list[-1].append("QUOTE")
            else:
                # Globbing of strings with asterisks
                globbing = glob(child.getText())
                if globbing:
                    self.command_list[-1].extend(globbing)
                else:
                    self.command_list[-1].append(child.getText())
        self.visitChildren(ctx)

        # Identifying if there was a subcommand or a quote within
        for i, s in enumerate(self.command_list[-1]):
            if s == "CMD":
                self.command_list[-1].pop(i)
                for args in self.output.popleft()[::-1]:
                    for subArgs in args.replace("\n", " ").rstrip().split(" ")[::-1]:
                        self.command_list[-1].insert(i, subArgs)
            elif s == "QUOTE":
                self.command_list[-1][i] = ''.join(self.temporary_quote.pop()[1:-1])
                

        if ctx.getChildCount() > 1:
            newArgs = []
            for i in range(ctx.getChildCount()):
                newArgs = [self.command_list[-1].pop()] + newArgs
            self.command_list[-1].append("".join(newArgs))

        # print(self.output)

        
                
    def visitQuoted(self, ctx:Comp0010ShellParser.QuotedContext):
        self.temporary_quote.append([])
        for child in ctx.getChildren():
            # Adding double quotes and single quotes ONLY
            if child.__class__.__name__ != "BackquoteContext":
                if child.getChild(0):
                    for child2 in child.getChildren():
                        # Creating a temporary placeholder
                        if child2.__class__.__name__ == "BackquoteContext":
                            self.temporary_quote[-1].append("CMD")
                        else:
                            self.temporary_quote[-1].append(child2.getText())
            else:
                self.temporary_quote.pop()

        self.visitChildren(ctx)

        # Identifying if there was a CMD within the quote
        if len(self.temporary_quote) > 0:
            for i, s in enumerate(self.temporary_quote[-1]):
                if s == "CMD":
                    self.temporary_quote[-1].pop(i)
                    for args in self.output.popleft()[::-1]:
                        for subArgs in args.replace("\n", " ").rstrip().split(" ")[::-1]:
                            self.temporary_quote[-1].insert(i, subArgs)


    def visitBackquote(self, ctx:Comp0010ShellParser.BackquoteContext):
        self.visitChildren(ctx)
        if ctx.getChild(1).getChildCount() == 3:
            if ctx.getChild(1).getChild(1).getText() == ";":
                count = 1
                node = ctx.getChild(1).getChild(0)
                while node.getChildCount() == 3 and node.getChild(1).getText() == ";":
                    count += 1
                    node = node.getChild(0)
                newOut = []
                for i in range(count + 1):
                    newOut = self.output.pop() + newOut
        
                self.output.append(newOut)

                

    def execute_commands(self, commands, out):
        # Execute the commands in the order of traversal
        command_executor = CommandExecutor()
        app = commands[0]
        args = commands[1:]

        # # Adding arguments from previous call in pipe to current call
        # args.extend(pipeArgs)

        if app in command_executor.command_map:
            command_executor.command_map[app].execute(args, out)
        else:
            raise ValueError(f"Unsupported application {app}") 

    

        

def parse(cmdline, out):
    input_stream = InputStream(io.StringIO(cmdline).read())
    lexer = Comp0010ShellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Comp0010ShellParser(stream)

    # Building tree
    tree = parser.command()
    
    # Working through tree
    visitor = Visitor()
    visitor.visit(tree)

    for i in visitor.output:
        out.extend(i)
    
def print_parse_tree(node, indent=""):
    if hasattr(node, 'children'):
        node_type = node.__class__.__name__
        print(node_type)
        for child in node.children:
            print_parse_tree(child, indent)
    else:
        print(" " + node.getText())
    
    
if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        out = deque()
        parse(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
    else:
      while True:
        print(os.getcwd() + "> ", end="")
        cmdline = input()
        out = deque()
        parse(cmdline, out)
        while len(out) > 0:
            print(out.popleft(), end="")

    if os.path.isfile(".temporary.txt"):
            os.remove(".temporary.txt")
