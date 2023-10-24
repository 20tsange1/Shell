import re
import sys
import os
from os import listdir
from collections import deque
from glob import glob

class Command:
    def execute(self, args, out):
        pass


class PwdCommand(Command):
    def execute(self, args, out):
        out.append(os.getcwd())


class CdCommand(Command):
    def execute(self, args, out):
        if len(args) == 0 or len(args) > 1:
            raise ValueError("Wrong number of command line arguments")
        os.chdir(args[0])


class EchoCommand(Command):
    def execute(self, args, out):
        out.append(" ".join(args) + "\n")


class LsCommand(Command):
    def execute(self, args, out):
        if len(args) == 0:
            ls_dir = os.getcwd()
        elif len(args) > 1:
            raise ValueError("Wrong number of command line arguments")
        else:
            ls_dir = args[0]
        for f in listdir(ls_dir):
            if not f.startswith("."):
                out.append(f + "\n")


class CatCommand(Command):
    def execute(self, args, out):
        for a in args:
            with open(a) as f:
                out.append(f.read())


class HeadCommand(Command):
    def execute(self, args, out):
        if len(args) != 1 and len(args) != 3:
            raise ValueError("Wrong number of command line arguments")
        if len(args) == 1:
            num_lines = 10
            file = args[0]
        if len(args) == 3:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        with open(file) as f:
            lines = f.readlines()
            for i in range(0, min(len(lines), num_lines)):
                out.append(lines[i])


class TailCommand(Command):
    def execute(self, args, out):
        if len(args) != 1 and len(args) != 3:
            raise ValueError("Wrong number of command line arguments")
        if len(args) == 1:
            num_lines = 10
            file = args[0]
        if len(args) == 3:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        with open(file) as f:
            lines = f.readlines()
            display_length = min(len(lines), num_lines)
            for i in range(0, display_length):
                out.append(lines[len(lines) - display_length + i])


class GrepCommand(Command):
    def execute(self, args, out):
        if len(args) < 2:
            raise ValueError("Wrong number of command line arguments")
        pattern = args[0]
        files = args[1:]
        for file in files:
            with open(file) as f:
                lines = f.readlines()
                for line in lines:
                    if re.match(pattern, line):
                        if len(files) > 1:
                            out.append(f"{file}:{line}")
                        else:
                            out.append(line)

                            
class SortCommand(Command):
    def execute(self, args, out):
        reverse = False
        filename = None

        for arg in args:
            if arg == '-r':
                reverse = True
            else:
                filename = arg

        if filename:
            with open(filename, 'r') as file:
                lines = file.readlines()
        else:
            #if no filename, read from stdin
            lines = sys.stdin.readlines()

        sorted_lines = sorted(lines, reverse=reverse)
        out.extend(sorted_lines)
                            
                            
class CutCommand(Command):
    def execute(self, args, out):
        if len(args) not in [1, 3]:
            raise ValueError("Wrong number of command line arguments")
        
        if len(args) == 1:
            bytes_range = args[0]
            lines = sys.stdin.readlines()
        else:
            if args[0] != "-b":
                raise ValueError("Wrong flags")
            bytes_range = args[1]
            with open(args[2], 'r') as file:
                lines = file.readlines()

        output = []
        for line in lines:
            line_output = []
            line = line.strip()
            byte_ranges = bytes_range.split(',')
            for byte_range in byte_ranges:
                if '-' in byte_range:
                    start, end = byte_range.split('-')
                    start = int(start) - 1 if start else None
                    end = int(end) if end else None
                    line_output.append(line[start:end])
                else:
                    pos = int(byte_range)
                    line_output.append(line[pos - 1])
            output.append(''.join(line_output))

        output.append('\n')
        out.extend(output)