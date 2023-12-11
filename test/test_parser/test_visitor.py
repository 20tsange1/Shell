import tempfile
import unittest
import os
from pathlib import Path
from shell import parse
from error import ArgumentError


class TestVisitor(unittest.TestCase):
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    def teardown(self):
        self.test_dir.cleanup()

    def test_call(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        parse("cat " + self.test_file[0], out)
        self.assertEqual(
            "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n", "".join(out)
        )
        self.teardown()

    def test_redirection_stdin(self):
        out = self.setup(["ABCDEFFEDCBA\nABCDDCBA\n"])
        parse("echo < " + self.test_file[0], out)
        self.assertEqual("ABCDEFFEDCBA\nABCDDCBA\n", "".join(out))
        self.teardown()

    def test_redirection_stdin_space(self):
        out = self.setup(["ABCDEFFEDCBA\nABCDDCBA\n"])
        parse("echo <" + self.test_file[0], out)
        self.assertEqual("ABCDEFFEDCBA\nABCDDCBA\n", "".join(out))
        self.teardown()

    def test_redirection_stdout(self):
        out = self.setup([""])
        parse("echo foo > " + self.test_file[0], out)
        with open(self.test_file[0], "r") as f:
            self.assertEqual("foo\n", f.read())
        self.teardown()

    def test_pipe(self):
        out = self.setup([])
        parse("echo foo | cat", out)
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_argument_quoted_single(self):
        out = self.setup([])
        parse("echo 'foo bar'", out)
        self.assertEqual("foo bar\n", "".join(out))
        self.teardown()

    def test_argument_quoted_double(self):
        out = self.setup([])
        parse('echo "foo bar"', out)
        self.assertEqual("foo bar\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote(self):
        out = self.setup([])
        parse("echo `echo foo`", out)
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote_multiarg(self):
        out = self.setup(["ccc\naaa\nbbb\n"])
        parse("echo `sort " + self.test_file[0] + "`", out)
        self.assertEqual("aaa bbb ccc\n", "".join(out))
        self.teardown()

    def test_argument_quoted_backquote_multiarg2(self):
        out = self.setup([])
        parse('echo `echo foo   "  hello"`', out)
        self.assertEqual("foo hello\n", "".join(out))
        self.teardown()

    def test_argument_multi(self):
        out = self.setup([])
        parse("echo foo'bar'", out)
        self.assertEqual("foobar\n", "".join(out))
        self.teardown()

    def test_argument_multi_backquote(self):
        out = self.setup([])
        parse("echo foo`echo bar`'hello'", out)
        self.assertEqual("foobarhello\n", "".join(out))
        self.teardown()

    def test_quoted_double_backquote(self):
        out = self.setup([])
        parse('echo "`echo foo`"', out)
        self.assertEqual("foo\n", "".join(out))
        self.teardown()

    def test_quoted_double_backquote_multi(self):
        out = self.setup([])
        parse('echo "`echo foo`bar"', out)
        self.assertEqual("foobar\n", "".join(out))
        self.teardown()

    def test_argument_glob(self):
        out = self.setup(["a", "b"])
        os.chdir(self.temp_path)
        parse("echo *", out)
        result = set(out[0].split())
        self.assertEqual({f"test-{i}.txt" for i in range(2)}, result)
        self.teardown()

    def test_argument_glob_multi(self):
        out = self.setup(["a", "b", "c"])
        os.chdir(self.temp_path)
        parse("echo *'.txt'", out)
        result = set(out[0].split())
        self.assertEqual({f"test-{i}.txt" for i in range(3)}, result)
        self.teardown()

    def test_globbing_no_match(self):
        out = self.setup([])
        os.chdir(self.temp_path)
        with self.assertRaises(ArgumentError):
            parse("echo *", out)
        self.teardown()

    def test_no_subarg(self):
        out = self.setup([])
        os.chdir(self.temp_path)
        parse("echo `echo foo | cut -b 5`", out)
        self.assertEqual("\n", "".join(out))
        self.teardown()
