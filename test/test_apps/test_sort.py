import tempfile
import unittest
from pathlib import Path
import sys
import random
import io
from apps.sort import Sort
from error import ArgumentError, FileError, FlagError
from hypothesis import given, strategies as st
from unittest.mock import patch


class TestSort(unittest.TestCase):
    def setup(self, contents):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        self.test_file = []
        self.saved_stdin = sys.stdin
        for i in range(len(contents)):
            self.test_file.append(str(self.temp_path) + f"/test-{i}.txt")
            with open(self.test_file[i], "w") as f:
                f.write(contents[i])
        return []

    def teardown(self):
        self.test_dir.cleanup()
        sys.stdin = self.saved_stdin

    def test_sort_file_ordered(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        Sort().execute([self.test_file[0]], out)
        self.assertEqual(
            "".join(out), "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        )
        self.teardown()

    def test_sort_file_unordered(self):
        out = self.setup(
            ["GGG\nBBB\nCCC\nDDD\nJJJ\nFFF\nEEE\nHHH\nAAA\nIII\n"]
        )
        Sort().execute([self.test_file[0]], out)
        self.assertEqual(
            "".join(out), "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        )
        self.teardown()

    def test_sort_file_ordered_reverse(self):
        out = self.setup(
            ["AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"]
        )
        Sort().execute(["-r", self.test_file[0]], out)
        self.assertEqual(
            "".join(out), "JJJ\nIII\nHHH\nGGG\nFFF\nEEE\nDDD\nCCC\nBBB\nAAA\n"
        )
        self.teardown()

    def test_sort_file_unordered_reverse(self):
        out = self.setup(
            ["GGG\nBBB\nCCC\nDDD\nJJJ\nFFF\nEEE\nHHH\nAAA\nIII\n"]
        )
        Sort().execute(["-r", self.test_file[0]], out)
        self.assertEqual(
            "".join(out), "JJJ\nIII\nHHH\nGGG\nFFF\nEEE\nDDD\nCCC\nBBB\nAAA\n"
        )
        self.teardown()

    def test_sort_file_unordered_length(self):
        out = self.setup(["ABCDEFGH\nABCDEFGHIJK\nABCDEF\n"])
        Sort().execute([self.test_file[0]], out)
        self.assertEqual("".join(out), "ABCDEF\nABCDEFGH\nABCDEFGHIJK\n")
        self.teardown()

    def test_sort_file_unordered_length_reverse(self):
        out = self.setup(["ABCDEFGH\nABCDEFGHIJK\nABCDEF\n"])
        Sort().execute(["-r", self.test_file[0]], out)
        self.assertEqual("".join(out), "ABCDEFGHIJK\nABCDEFGH\nABCDEF\n")
        self.teardown()

    def test_sort_file_unordered_dynamic(self):
        temp = [str(random.randint(0, 100)) for i in range(100)]
        out = self.setup(["\n".join(temp)])
        Sort().execute([self.test_file[0]], out)
        self.assertEqual("".join(out), "\n".join(sorted(temp)) + "\n")
        self.teardown()

    def test_sort_file_unordered_dynamic_reverse(self):
        temp = [str(random.randint(0, 100)) for i in range(100)]
        out = self.setup(["\n".join(temp)])
        Sort().execute(["-r", self.test_file[0]], out)
        self.assertEqual(
            "".join(out), "\n".join(sorted(temp, reverse=True)) + "\n"
        )
        self.teardown()

    def test_sort_empty(self):
        out = self.setup([""])
        Sort().execute([self.test_file[0]], out)
        self.assertEqual("".join(out), "")
        self.teardown()

    def test_sort_empty_reverse(self):
        out = self.setup([""])
        Sort().execute(["-r", self.test_file[0]], out)
        self.assertEqual("".join(out), "")
        self.teardown()

    def test_sort_wrong_arguments(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(ArgumentError):
            Sort().execute(["-c", self.test_file[0], self.test_file[1]], out)
        self.teardown()

    def test_sort_stdin(self):
        out = self.setup(["GGG\nBBB\nCCC\nDDD\nJJJ\nFFF\nEEE\nHHH\nAAA\nIII\n"])
        with patch("sys.stdin", open(self.test_file[0])):
            Sort().execute([], out)
        self.assertEqual(
            "".join(out), "AAA\nBBB\nCCC\nDDD\nEEE\nFFF\nGGG\nHHH\nIII\nJJJ\n"
        )
        self.teardown()

    def test_sort_stdin_reverse(self):
        out = self.setup(["GGG\nBBB\nCCC\nDDD\nJJJ\nFFF\nEEE\nHHH\nAAA\nIII\n"])
        with patch("sys.stdin", open(self.test_file[0])):
            Sort().execute(["-r"], out)
        self.assertEqual(
            "".join(out), "JJJ\nIII\nHHH\nGGG\nFFF\nEEE\nDDD\nCCC\nBBB\nAAA\n"
        )
        self.teardown()

    def test_sort_invalid_file(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(FileError):
            Sort().execute(["invalidfile.txt"], out)
        self.teardown()

    def test_sort_invalid_flag(self):
        out = self.setup(["a", "b"])
        with self.assertRaises(FlagError):
            Sort().execute(["-c", "invalidfile.txt"], out)
        self.teardown()

    # Hypothesis tests
    # Equal length property testing
    @given(
        st.lists(
            st.text(
                min_size=1,
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=1,
        ),
    )
    def test_sort_hypothesis(self, contents):
        out = self.setup(["\n".join(contents) + "\n"])
        Sort().execute([self.test_file[0]], out)
        self.assertEqual(len(out), len(contents))
        self.teardown()

    # Testing if the output is sorted
    @given(
        st.lists(
            st.text(
                min_size=1,
                alphabet=st.characters(
                    whitelist_categories=("Ll", "Lu", "Nd"),
                ),
            ),
            min_size=1,
        ),
    )
    def test_sort_hypothesis_sorted(self, contents):
        out = self.setup(["\n".join(contents) + "\n"])
        Sort().execute([self.test_file[0]], out)
        self.assertEqual("".join(out), "\n".join(sorted(contents)) + "\n")
        self.teardown()
