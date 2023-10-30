import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob
from commands import *;
from io_redirection import *;
import readline


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
            

class CommandParser:
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
    
    # ISSUE (but works for some reason): input is never restored for either io redirection
    def redirect_output(self, args, app, append=False):
        index = args.index('>')
        if index == len(args) - 1:
            raise ValueError("No output file specified")
        else:
            # print(args[index+1])
            output_redirector = OutputRedirection(args[index + 1], append)
            output_redirector.redirect_output()
            self.command_map[app].execute(args[:index], out)
            # output_redirector.restore_output()
            
    def redirect_input(self, args, app):
        index = args.index('<')
        if index == len(args) - 1:
            raise ValueError("No input file specified")
        else:
            input_redirector = InputRedirection(args[index + 1])
            input_redirector.redirect_input()
            self.command_map[app].execute(args[:index], out)
            # input_redirector.restore_input()

    def parse(self, cmdline, out):
        # regex1 = "([^\"'`;]+|\"[^\"]*\"|'[^']*'|`[^`]*`)"
        regex1test = "([^;]+)"
        regex2 = "[^\\s\"'`]+|\"([^\"]*)\"|'([^']*)'|`([^`]*)`"
        
        pipe_segments = cmdline.split("|")
        prev_out = None
        for segment in pipe_segments:
            segment = segment.rstrip().lstrip()
            temp_out = deque() if prev_out is None else prev_out
            raw_commands = []
            
            for m in re.finditer(regex1test, segment):
                if m.group(0):
                    raw_commands.append(m.group(0))
            for i, command in enumerate(raw_commands):
                tokens = []
                for m in re.finditer(regex2, command):
                    if m.group(1) or m.group(2):
                        quoted = m.group(0)
                        tokens.append(quoted[1:-1])
                    elif m.group(3):
                        quoted = m.group(0)
                        tokens.extend(self.parseHandle(quoted[1:-1]))
                    else:
                        globbing = glob(m.group(0))
                        if globbing:
                            tokens.extend(globbing)
                        else:
                            tokens.append(m.group(0))
                app = tokens[0]
                args = tokens[1:]
                
                if '>' in args:
                    self.redirect_output(args, app, False)
                elif '<' in args:
                    self.redirect_input(args, app)
                else:
                    if app in self.command_map:
                        if prev_out is not None and i == 0:
                            args.append(prev_out.popleft())  # pass relayed input as last argument
                        self.command_map[app].execute(args, temp_out)
                    else:
                        raise ValueError(f"Unsupported application {app}")
                    
            prev_out = temp_out
        out.extend(prev_out)

    def parseHandle(self, cmdline):
        output = []
        self.parse(cmdline, output)
        output = ''.join(output).split(' ')
        for i in range(len(output)):
            output[i] = output[i].replace("\n", ' ').rstrip()
        return output


if __name__ == "__main__":
    args_num = len(sys.argv) - 1
    parser = CommandParser()
    
    if args_num > 0:
        if args_num != 2:
            raise ValueError("wrong number of command line arguments")
        if sys.argv[1] != "-c":
            raise ValueError(f"unexpected command line argument {sys.argv[1]}")
        out = deque()
        parser.parse(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
            
    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            parser.parse(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")

