import tempfile
import unittest
from pathlib import Path
from apps.echo import Echo
from unittest.mock import patch
from hypothesis import given, strategies as st


class TestEcho(unittest.TestCase):
    def setup(self):
        return []
      
    def setup_with_files(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    def test_echo(self):
        out = self.setup()
        Echo().execute(["foo"], out)
        self.assertEqual("".join(out), "foo\n")

    def test_echo_two(self):
        out = self.setup()
        Echo().execute(["hello", "world"], out)
        self.assertEqual("".join(out), "hello world\n")

    def test_echo_multi(self):
        out = self.setup()
        Echo().execute(["hello", "world", "echo", "foo"], out)
        self.assertEqual("".join(out), "hello world echo foo\n")

    def test_echo_numbers(self):
        out = self.setup()
        Echo().execute([str(i) for i in range(10)], out)
        self.assertEqual(
            "".join(out), " ".join([str(i) for i in range(10)]) + "\n"
        )

    def test_echo_keywords(self):
        out = self.setup()
        Echo().execute([";", "|", "'", '"', "`", "<", ">"], out)
        self.assertEqual("".join(out), "; | ' \" ` < >\n")

    def test_echo_special_characters(self):
        out = self.setup()
        Echo().execute(["!@#$%"], out)
        self.assertEqual("".join(out), "!@#$%\n")

    def test_echo_whitespace(self):
        out = self.setup()
        Echo().execute(["          "], out)
        self.assertEqual("".join(out), "          \n")

    def test_echo_newline(self):
        out = self.setup()
        Echo().execute(["Hello\nWorld"], out)
        self.assertEqual("".join(out), "Hello\nWorld\n")

    def test_echo_tabs(self):
        out = self.setup()
        Echo().execute(["Hello\tWorld"], out)
        self.assertEqual("".join(out), "Hello\tWorld\n")

    def test_echo_stdin(self):
        out = self.setup_with_files(["Hello World"])
        with patch("sys.stdin", open(self.test_file[0])):
            Echo().execute([], out)
        self.assertEqual("".join(out), "Hello World")

    # Hypothesis Testing
    # Checking if the output has a whitespace for each argument
    @given(st.lists(st.text(min_size=1), min_size=1))
    def test_echo_hypothesis(self, args):
        out = self.setup()
        Echo().execute(args, out)
        assert len(out[0]) == len("".join(args)) + len(args)
