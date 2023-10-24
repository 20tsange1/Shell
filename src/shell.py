import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob
from commands import *;

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
        }
        #add unsafe commands to map
        if (unsafe):
            self.add_unsafe_commands()

    def parse(self, cmdline, out):
        raw_commands = []
        for m in re.finditer("([^\"';]+|\"[^\"]*\"|'[^']*')", cmdline):
            if m.group(0):
                raw_commands.append(m.group(0))
        for command in raw_commands:
            tokens = []
            for m in re.finditer("[^\\s\"']+|\"([^\"]*)\"|'([^']*)'", command):
                if m.group(1) or m.group(2):
                    quoted = m.group(0)
                    tokens.append(quoted[1:-1])
                else:
                    globbing = glob(m.group(0))
                    if globbing:
                        tokens.extend(globbing)
                    else:
                        tokens.append(m.group(0))
            app = tokens[0]
            args = tokens[1:]
            if app in self.command_map:
                self.command_map[app].execute(args, out)
            else:
                raise ValueError(f"Unsupported application {app}")


if __name__ == "__main__":
    parser = CommandParser()
    while True:
        print(os.getcwd() + "> ", end="")
        cmdline = input()
        out = deque()
        parser.parse(cmdline, out)
        while len(out) > 0:
            print(out.popleft(), end="")