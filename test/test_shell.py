import unittest

from shell import parse
from collections import deque


class TestShell(unittest.TestCase):
    def test_shell(self):
        out = deque()
        parse("echo foo", out)
        self.assertEqual(''.join(out), "foo")

    def test_quoting_1(self):
        out = deque()
        parse('ec`echo "ho"` "hello"', out)
        self.assertEqual(''.join(out), "hello")

    def test_quoting_2(self):
        out = deque()
        parse('echo `echo "hello"`', out)
        self.assertEqual(''.join(out), "hello")

    def test_quoting_3(self):
        out = deque()
        parse('echo "hello `echo "hello"` hello"', out)
        self.assertEqual(''.join(out), "hello hello hello")
    
    def test_quoting_4(self):
        out = deque()
        parse('echo "hello `echo "bye"` hello"', out)
        self.assertEqual(''.join(out), "hello bye hello")

    def test_quoting_5(self):
        out = deque()
        parse('echo "hello `echo "bye"` hello `echo "bye"`"', out)
        self.assertEqual(''.join(out), "hello bye hello bye")

    def test_quoting_6(self):
        out = deque()
        parse('echo `echo foo | echo`', out)
        self.assertEqual(''.join(out), "foo")

    def test_substitution_semicolon_multi(self):
        out = deque()
        parse('echo `echo foo ; echo bar ; echo see ; echo bye`', out)
        self.assertEqual(''.join(out), "foo bar see bye")



if __name__ == "__main__":
    unittest.main()

# test case: ec`echo "ho"` "hello"

# cat *.txt | sort | uniq

# echo `cat *.txt | sort | uniq` ; echo `ls | sort | uniq`