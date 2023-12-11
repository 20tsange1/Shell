import unittest
from apps.color import Color
from error import ArgumentError, FlagError


class TestColor(unittest.TestCase):
    def setup(self):
        return []

    def teardown(self):
        print("\033[0m")
        pass

    def test_color(self):
        out = self.setup()
        Color().execute(["red"], out)
        self.assertEqual("".join(out), "\033[31m")
        self.teardown()

    def test_color_invalid(self):
        out = self.setup()
        with self.assertRaises(FlagError):
            Color().execute(["darkgrey"], out)
        self.teardown()

    def test_color_too_many_args(self):
        out = self.setup()
        with self.assertRaises(ArgumentError):
            Color().execute(["red", "blue", "green"], out)
        self.teardown()
