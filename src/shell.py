import re
import sys
import os
import io
from os import listdir
from collections import deque
from glob import glob
from commands import *
from io_redirection import *
import tempfile
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
    def redirect_output(self, tokens, append=False):
        index = tokens.index('>')
        if index == len(tokens) - 1:
            raise ValueError("No output file specified")
        else:
            # print(args[index+1])
            path = tokens[index + 1]
            del tokens[index:index+2]
            
            app = tokens[0]
            args = tokens[1:]
            
            output_redirector = OutputRedirection(path, append)
            output_redirector.redirect_output()
            # self.command_map[app].execute(args[:index] + args[index + 2:], out)
            return output_redirector, app, args
            
    def redirect_input(self, tokens):
        index = tokens.index('<')

        if index == len(tokens) - 1:
            raise ValueError("No input file specified")
        else:
            path = tokens[index + 1]
            del tokens[index:index+2]
            
            app = tokens[0]
            args = tokens[1:]
            # print(app)
            input_redirector = InputRedirection(path)
            input_redirector.redirect_input()
            return input_redirector, app, args

    def parse(self, cmdline, out):
        # regex1 = "([^\"'`;]+|\"[^\"]*\"|'[^']*'|`[^`]*`)"
        regex1test = "([^;]+)"
        regex2 = "[^\\s\"'`]+|\"([^\"]*)\"|'([^']*)'|`([^`]*)`"
        
        pipe_segments = cmdline.split("|")
        prev_out = None
        temp_files = []
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
                            if (m.group(0).startswith('<') or m.group(0).startswith('>')) and len(m.group(0)) > 1:
                                tokens.append(m.group(0)[0])
                                tokens.append(m.group(0)[1:])  
                            else:
                                tokens.append(m.group(0))
                
                app = tokens[0]
                args = tokens[1:]
                
                redirector = None
                if '>' in tokens:
                    redirector, app, args = self.redirect_output(tokens, False)
                if '<' in tokens:
                    redirector, app, args = self.redirect_input(tokens)

                if app in self.command_map:
                    if prev_out is not None and i == 0:
                        # pass relayed input as last argument (now defunct)
                        # create a temporary file and write the contents of prev_out
                        with tempfile.NamedTemporaryFile(mode="w", delete=False) as tmp_file:
                            tmp_file.write(prev_out.popleft())
                            temp_files.append(tmp_file.name)
                        args.append(tmp_file.name)

                    self.command_map[app].execute(args, temp_out)
                else:
                    raise ValueError(f"Unsupported application {app}")                   
            prev_out = temp_out

        # Delete all the temporary files
        for tmp_file in temp_files:
            os.remove(tmp_file)

        out.extend(prev_out)
        return redirector


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
        redirector = parser.parse(sys.argv[2], out)
        while len(out) > 0:
            print(out.popleft(), end="")
        if (redirector):
                redirector.restore()

    else:
        while True:
            print(os.getcwd() + "> ", end="")
            cmdline = input()
            out = deque()
            redirector = parser.parse(cmdline, out)
            while len(out) > 0:
                print(out.popleft(), end="")
            if (redirector):
                redirector.restore()


