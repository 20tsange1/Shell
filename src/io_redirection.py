import sys


class InputRedirection:
    def __init__(self, input_file=None):
        self.input_file = input_file
        self.saved_stdin = sys.stdin

    def redirect_input(self):
        self.input_stream = open(self.input_file, "r")
        sys.stdin = self.input_stream
        # for line in sys.stdin:
        #     res = args.append(line.strip())

    def restore(self, *args):
        sys.stdin = self.saved_stdin
        self.input_stream.close()


class OutputRedirection:
    def __init__(self, output_file=None, append=False):
        self.output_file = output_file
        self.append = append
        self.saved_stdout = sys.stdout

    # def redirect_output(self):
    #     mode = "a" if self.append else "w"
    #     self.output_stream = open(self.output_file, mode)
    #     sys.stdout = self.output_stream

    def redirect_output(self, output):
        with open(self.output_file, "w") as stdout:
            stdout.write(''.join(output))

    def restore(self, *args):
        sys.stdout = self.saved_stdout
        self.output_stream.close()