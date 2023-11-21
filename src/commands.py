import re
import sys
import os
import fnmatch
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
        if len(args) == 0:
            out.extend(sys.stdin.readlines())
        else:
            for a in args:
                with open(a) as f:
                    # out.append(f.read())
                    out.extend(f.readlines())
            if (len(out) > 0 and out[-1][-1] != '\n'):
                  out[-1] += '\n'   


class HeadCommand(Command):
    def execute(self, args, out):
        if len(args) > 3:
            raise ValueError("Wrong number of command line arguments")
        file = None

        if len(args) == 0:
            num_lines = 10
            

        elif len(args) == 1:
            num_lines = 10
            file = args[0]

        elif len(args) == 2:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])
        
        elif len(args) == 3:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        
        if file:
            with open(file) as f:
                lines = f.readlines()
                for i in range(0, min(len(lines), num_lines)):
                    out.append(lines[i])
        else:
            lines = sys.stdin.readlines()
            for i in range(0, min(len(lines), num_lines)):
                out.append(lines[i])


class TailCommand(Command):
    def execute(self, args, out):
        if len(args) > 3:
            raise ValueError("Wrong number of command line arguments")

        file = None

        if len(args) == 0:
            num_lines = 10

        elif len(args) == 1:
            num_lines = 10
            file = args[0]
        
        elif len(args) == 2:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])

        elif len(args) == 3:
            if args[0] != "-n":
                raise ValueError("Wrong flags")
            else:
                num_lines = int(args[1])
                file = args[2]
        
        if file:
            with open(file) as f:
                lines = f.readlines()
                display_length = min(len(lines), num_lines)
                for i in range(0, display_length):
                    out.append(lines[len(lines) - display_length + i])
        else:
            lines = sys.stdin.readlines()
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

        if (len(args) > 2):
            raise ValueError("Wrong number of command line arguments")

        for arg in args:
            if arg == '-r':
                reverse = True
            else:
                filename = arg

        if filename:
            with open(filename, 'r') as file:
                lines = file.readlines()
                if (len(lines) > 0 and lines[-1][-1] != '\n'):
                    lines[-1] += '\n'

        else:
            # if no filename, read from stdin
            lines = sys.stdin.readlines()

        sorted_lines = sorted(lines, reverse=reverse)

        out.extend(sorted_lines)


class CutCommand(Command):
    def execute(self, args, out):
        if len(args) == 0 or len(args) > 3:
            raise ValueError("Wrong number of command line arguments")

        if args[0] != "-b":
            raise ValueError("Wrong flag")
        
        bytes_range = args[1]    
        if len(args) == 2:
            lines = sys.stdin.readlines()
        else:
            with open(args[2], 'r') as file:
                lines = file.readlines()

        byte_ranges = bytes_range.split(',')
        for line in lines:
            line_output = []
            line = line.strip()
            for byte_range in byte_ranges:
                if '-' in byte_range:
                    start, end = byte_range.split('-')
                    start = int(start) - 1 if start else None
                    end = int(end) if end else None
                    line_output.append(line[start:end])
                else:
                    pos = int(byte_range)
                    line_output.append(line[pos - 1])
            
            out.extend(line_output)
            out.append('\n')


class FindCommand(Command):

    def find(self, dire, prev, item, found, flag):
        if os.path.isdir(dire):
            os.chdir(dire)
            if flag:
                for f in listdir(dire):
                    if not f.startswith("."):
                        self.find(os.path.join(dire, f), os.path.join(prev, f), item, found, True)
                        found.append(prev + "/" + f + "\n")
            else:
                for f in listdir(dire):
                    if fnmatch.fnmatch(f, item):
                        self.find(os.path.join(dire, f), os.path.join(prev, f), item, found, True)
                        found.append(prev + "/" + f + "\n")
                    else:
                        self.find(os.path.join(dire, f), os.path.join(prev, f), item, found, False)

    def execute(self, args, out):
        if len(args) == 0 or len(args) > 3:
            raise ValueError("Wrong number of command line arguments")
        else:
            # Without PATH name.
            if len(args) == 2 and args[0] == "-name":
                ls_dir = os.getcwd()
                self.find(ls_dir, ".", args[1], out, False)
                os.chdir(ls_dir)

            # With PATH name.
            elif len(args) == 3 and args[1] == "-name":
                ls_dir = os.getcwd()
                if os.path.isdir(ls_dir):
                    self.find(os.path.join(ls_dir, args[0]), os.path.join(args[0]), args[2], out, False)
                    os.chdir(ls_dir)
                else:
                    raise ValueError("Invalid Directory Name")
            else:
                raise ValueError("Wrong Flags")
        

class UniqCommand(Command):
    def return_uniq(self, lines, ignore_case):
        return_text = []
        for i in range(1, len(lines)):
            if ignore_case:
                if lines[i].strip("\n").lower() != lines[i - 1].strip("\n").lower():
                    return_text.append(lines[i].strip("\n") + "\n")
            else:
                if lines[i].strip("\n") != lines[i - 1].strip("\n"):
                    return_text.append(lines[i].strip("\n") + "\n")
        return return_text

    def unique_file(self, file_name, ignore_case):
        with open(file_name, 'r') as file:
            lines = [""] + file.readlines()
        return self.return_uniq(lines, ignore_case)

    # def unique_stdin(self, ignore_case, args):
    def unique_stdin(self, ignore_case):
        lines = [""] + sys.stdin.readlines()
        return self.return_uniq(lines, ignore_case)

    def execute(self, args, out):
        if len(args) == 0:
            out.extend(self.unique_stdin(False))
        elif len(args) == 1:
            if args[0] == '-i':
                out.extend(self.unique_stdin(True))
            elif os.path.isfile(args[0]):
                out.extend(self.unique_file(args[0], False))
            else:
                raise ValueError("Wrong flags or invalid file")
        elif len(args) == 2:
            if args[0] == '-i' and os.path.isfile(args[1]):
                out.extend(self.unique_file(args[1], True))
            elif args[0] != '-i':
                raise ValueError("Wrong flags")
        else:
            raise ValueError("Wrong number of command line arguments")
            