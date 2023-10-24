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

class FindCommand(Command):        
    def execute(self, args, out):
        found = []

        def findItem(directoryName, itemName, prev, found):
            if os.path.isdir(directoryName):
                for f in listdir(directoryName):
                    if not f.startswith("."):
                        if itemName in prev or itemName in f:
                            found.append(prev + "/" + f)
                        findItem(prev + "/" + f, itemName, prev + "/" + f, found)
        
        if len(args) == 0 or len(args) > 3:
            raise ValueError("wrong number of command line arguments")
        else:
            # Without PATH name.
            if len(args) == 2 and args[0] == "-name":
                ls_dir = os.getcwd()
                find = args[1].strip('"*')
                findItem(ls_dir, find, ".", found)

            # With PATH name.
            elif len(args) == 3 and args[1] == "-name":
                ls_dir = args[0]
                if os.path.isdir(ls_dir):
                    find = args[2].strip('"*')
                    findItem(ls_dir, find, ls_dir, found)
                else:
                    raise ValueError("Invalid Directory Name")
            else:
                raise ValueError("Wrong Flags")

        for i in found:
            out.append(i + "\n")
