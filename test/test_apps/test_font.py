import unittest
from apps.font import Font
from error import ArgumentError, FlagError


class TestFont(unittest.TestCase):
    def setup(self):
        return []

    def teardown(self):
        print("\033[0m")
        pass

    def test_font(self):
        out = self.setup()
        Font().execute(["bold"], out)
        self.assertEqual("".join(out), "\033[1m")
        self.teardown()

    def test_font_invalid(self):
        out = self.setup()
        with self.assertRaises(FlagError):
            Font().execute(["boldunderline"], out)
        self.teardown()

    def test_font_no_args(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Font().execute([], out)
        self.teardown()

    def test_font_too_many_args(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Font().execute(["underline", "bold"], out)
        self.teardown()
