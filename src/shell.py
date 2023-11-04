import sys
import os
import io
from collections import deque
from antlr4 import *
from commands import *
from io_redirection import *
from antlr.Comp0010ShellLexer import Comp0010ShellLexer
from antlr.Comp0010ShellParser import Comp0010ShellParser
from antlr.Comp0010ShellListener import Comp0010ShellListener


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
class Visitor(Comp0010ShellListener):
    def __init__(self):
        self.command_list = []  # Maintain a list of commands and their arguments

    #OVERRIDDEN METHODS
    
    def enterFunction(self, ctx: Comp0010ShellParser.FunctionContext):
        # When entering a function context, create a command tuple and add it to the list
        command = ctx.getText()
        self.command_list.append((command, []))

    def enterArgument(self, ctx: Comp0010ShellParser.ArgumentContext):
        # add arguments to command list tuple
        for child in ctx.getChildren():
            # if child is not of type QuotedContext
            if child.__class__.__name__ != "QuotedContext":
                argument = child.getText()
                self.command_list[-1][1].append(argument)
    
    def enterQuoted(self, ctx: Comp0010ShellParser.QuotedContext):
        # remove the quotes from ctx.getText()
        self.command_list[-1][1].append(ctx.getText()[1:-1])
        
    #TODO: implement io redirection here. Use exitRedirection if necessary
    def enterRedirection(self, ctx: Comp0010ShellParser.RedirectionContext):
        file = ctx.getChild(1).getText()
        if ctx.getChild(0).getText() == ">":
            output_redirection = OutputRedirection(file, False)
            output_redirection.redirect_output()
        elif ctx.getChild(0).getText() == "<":
            input_redirection = InputRedirection(file)
            input_redirection.redirect_output()

    
    def exitRedirection(self, ctx: Comp0010ShellParser.RedirectionContext):
        # restore the redirection
        
        
          
    
    #TODO: implement command substitution here. Use exitsubcmd if necessary
    def enterSubcmd(self, ctx: Comp0010ShellParser.CommandContext):
        pass
    
            
    #TODO: implement pipe operator here. Use exitPipe if necessary
    def enterPipe(self, ctx: Comp0010ShellParser.PipeContext):
        pass
      
      
      

    #HELPER METHODS

    def execute_commands(self, out):
        # Execute the commands in the order of traversal
        command_executor = CommandExecutor()
        for app, args in self.command_list:
            if app in command_executor.command_map:
                command_executor.command_map[app].execute(args, out)
            else:
                raise ValueError(f"Unsupported application {app}") 
        

def parse(cmdline, out):
    input_stream = InputStream(io.StringIO(cmdline).read())
    lexer = Comp0010ShellLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = Comp0010ShellParser(stream)
    tree = parser.command()
    # print_parse_tree(tree)
    
    visitor = Visitor()
    walker = ParseTreeWalker()
    walker.walk(visitor, tree)
    visitor.execute_commands(out)
    
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