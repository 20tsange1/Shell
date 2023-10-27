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
        out.append(os.getcwd() + "\n")


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
        out.append("\n")


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
                lines[-1] += '\n' if (lines[-1][-1] != '\n') else '' 

        else:
            # if no filename, read from stdin
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


class FindCommand(Command):
    # Needs to be made more precise
    def findItem(self, directoryName, itemName, prev, flag, exact, out):
        if os.path.isdir(directoryName):
            for f in listdir(directoryName):
                if not f.startswith("."):
                    if (not flag) and ((exact and (itemName == f)) or ((not exact) and (itemName in f))):
                        out.append(prev + "/" + f + "\n")
                        self.findItem(prev+"/"+f, itemName, prev+"/"+f, True, exact, out)
                    elif flag:
                        out.append(prev + "/" + f + "\n")
                        self.findItem(prev+"/"+f, itemName, prev+"/"+f, True, exact, out)
                    else:
                        self.findItem(prev+"/"+f, itemName, prev+"/"+f, False, exact, out)

        out.extend(output) 
        

class UniqCommand(Command):
    def returnUniq(self, lines, ignore):
        returnText = ""
        for i in range(1, len(lines)):
            if ignore:
                if lines[i].strip("\n").lower() != lines[i-1].strip("\n").lower():
                    returnText += lines[i].strip("\n") + "\n"
            else:
                if lines[i].strip("\n") != lines[i - 1].strip("\n"):
                    returnText += lines[i].strip("\n") + "\n"
        return returnText[0:-1]

    def uniqueFile(self, fileName, ignore):
        with open(fileName, 'r') as file:
            lines = [""] + file.readlines()

        # with open(fileName, 'w') as file:
        #     file.write(returnUniq(lines, ignore))
        return self.returnUniq(lines, ignore)

    def uniqueStdin(self, ignore):
        lines = [""] + sys.stdin.readlines()
        return self.returnUniq(lines, ignore)

    def execute(self, args, out):
        if len(args) == 0:
            out.append(self.uniqueStdin(False) + "\n")
        elif len(args) == 1:
            if args[0] == '-i':
                out.append(self.uniqueStdin(True) + "\n")
            elif os.path.isfile(args[0]):
                out.append(self.uniqueFile(args[0], False) + "\n")
            else:
                raise ValueError("Wrong flags or invalid file")
        elif len(args) == 2:
            if args[0] == '-i' and os.path.isfile(args[1]):
                out.append(self.uniqueFile(args[1], True) + "\n")
            elif args[0] != '-i':
                raise ValueError("Wrong flags")
        else:
            raise ValueError("Wrong number of command line arguments")

        for i in found:
            out.append(i + "\n")