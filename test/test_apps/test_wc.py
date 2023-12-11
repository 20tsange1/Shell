import tempfile
import unittest
from hypothesis import given, strategies as st
from unittest.mock import patch
from pathlib import Path
from apps.wc import Wc
from error import FileError, FlagError


class TestWc(unittest.TestCase):
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path / f"test-{i}.txt"))
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])

    def teardown(self):
        self.test_dir.cleanup()

    def test_wc_count_lines(self):
        self.setup(["Line 1\nLine 2\nLine 3"])
        out = []
        Wc().execute(["-l"] + self.test_file, out)
        self.assertEqual(out, ["3\n"])
        self.teardown()

    def test_wc_count_words(self):
        self.setup(["This is a sample text for word count."])
        out = []
        Wc().execute(["-w"] + self.test_file, out)
        self.assertEqual(out, ["8" + "\n"])
        self.teardown()

    def test_wc_count_characters(self):
        self.setup(["Hello, World!"])
        out = []
        Wc().execute(["-m"] + self.test_file, out)
        self.assertEqual(out, ["13" + "\n"])
        self.teardown()

    def test_wc_multiple_options(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        Wc().execute([] + self.test_file, out)
        expected_output = ["1\n", "6\n", "40\n"]
        self.assertEqual(out, expected_output)
        self.teardown()

    def test_wc_stdin(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        with patch("sys.stdin", open(self.test_file[0])):
            Wc().execute([], out)
        expected_output = ["1\n", "6\n", "40\n"]
        self.assertEqual(out, expected_output)
        self.teardown()

    def test_wc_stdin_with_flags(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        with patch("sys.stdin", open(self.test_file[0])):
            Wc().execute(["-l"], out)
        expected_output = ["1" + "\n"]
        self.assertEqual(out, expected_output)
        self.teardown()

    def test_wc_wrong_arguments(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        with self.assertRaises(FlagError):
            Wc().execute(["-x"] + self.test_file, out)
        self.teardown()

    def test_wc_nonexistent_file_without_flags(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        with self.assertRaises(FileError):
            Wc().execute(["nonexistent_file.txt"], out)
        self.teardown()

    def test_wc_nonexistent_file_with_flags(self):
        self.setup(["Multiple options for testing wc command."])
        out = []
        with self.assertRaises(FileError):
            Wc().execute(["-l", "nonexistent_file.txt"], out)
        self.teardown()

    # Hypothesis tests
    # more or equal chars to words invariant
    @given(
        st.text(
            alphabet=st.characters(
                whitelist_categories=("Ll", "Lu", "Nd"),
            ),
        ),
    )
    def test_wc_chars_more_or_equal_words_invariant(self, contents):
        if len(contents) == 0:
            return
        self.setup(contents)
        out = []
        out2 = []
        Wc().execute(["-m"] + self.test_file, out)
        Wc().execute(["-w"] + self.test_file, out2)
        self.assertLessEqual("".join(out2), "".join(out))
        self.teardown()
