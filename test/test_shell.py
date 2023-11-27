import unittest
import os

from shell import parse
from collections import deque


class TestShell(unittest.TestCase):
    def test_echo_1(self):
        out = deque()
        parse("echo foo", out)
        self.assertEqual(''.join(out).rstrip(), "foo")

    def test_pwd_1(self):
        out = deque()
        parse("pwd", out)
        self.assertEqual(''.join(out).rstrip(), os.getcwd())

    def test_cd_1(self):
        out = deque()
        parse("cd src ; pwd", out)
        self.assertEqual(''.join(out).rstrip(), os.getcwd())

    # Testing Quoting

    def test_quoting_1(self):
        out = deque()
        parse('ec`echo "ho"` "hello"', out)
        self.assertEqual(''.join(out).rstrip(), "hello")

    def test_quoting_2(self):
        out = deque()
        parse('echo `echo "hello"`', out)
        self.assertEqual(''.join(out).rstrip(), "hello")

    def test_quoting_3(self):
        out = deque()
        parse('echo "hello `echo "hello"` hello"', out)
        self.assertEqual(''.join(out).rstrip(), "hello hello hello")
    
    def test_quoting_4(self):
        out = deque()
        parse('echo "hello `echo "bye"` hello"', out)
        self.assertEqual(''.join(out).rstrip(), "hello bye hello")

    # def test_quoting_5(self):
    #     out = deque()
    #     parse('echo "hello `echo "bye"` hello `echo "bye"`"', out)
    #     self.assertEqual(''.join(out).rstrip(), "hello bye hello bye")

    def test_quoting_6(self):
        out = deque()
        parse('echo `echo foo | echo`', out)
        self.assertEqual(''.join(out).rstrip(), "foo")

    def test_quoting_7(self):
        out = deque()
        parse('echo "hello   foo bar"', out)
        self.assertEqual(''.join(out).rstrip(), "hello   foo bar")

    def test_quoting_8(self):
        out = deque()
        parse('echo `echo hello    foo`', out)
        self.assertEqual(''.join(out).rstrip(), "hello foo")

    def test_quoting_innersub(self):
        out = deque()
        parse('echo hello`echo foo space bar`hello', out)
        self.assertEqual(''.join(out).rstrip(), "hellofoo space barhello")
    
    def test_quoting_innersub2(self):
        out = deque()
        parse('echo hello`echo "foo space bar"`hello', out)
        self.assertEqual(''.join(out).rstrip(), "hellofoo space barhello")
    
    def test_quoting_innersub_space(self):
        out = deque()
        parse('echo hello`echo "foo    space bar"`hello', out)
        self.assertEqual(''.join(out).rstrip(), "hellofoo space barhello")

    def test_substitution_semicolon_multi(self):
        out = deque()
        parse('echo `echo foo ; echo bar ; echo see ; echo bye`', out)
        self.assertEqual(''.join(out).rstrip(), "foo bar see bye")

    def test_substitution_semicolon_multi(self):
        out = deque()
        parse('ec`echo "ho"` "foo `echo bar`"', out)
        self.assertEqual(''.join(out).rstrip(), "foo bar")
    

    # def test_cut_single(self):
    #     out = deque()
    #     parse('', out)
    #     self.assertEqual(''.join(out).rstrip(), "")



if __name__ == "__main__":
    unittest.main()

# test case: ec`echo "ho"` "hello"

# cat *.txt | sort | uniq

# echo `cat *.txt | sort | uniq` ; echo `ls | sort | uniq`

# cut -b 3 testfiles/hello3.txt

# cut -b 1,3,5 testfiles/hello3.txt

# cut -b -3 testfiles/hello3.txt

# cut -b 4- testfiles/hello3.txt

# cut -b 1-3,3- testfiles/hello3.txt

# cut -b 2,3,2- testfiles/hello3.txt

# cut -b 4,8,6- testfiles/hello3.txt

# cut -b -3,1-2,4 testfiles/hello3.txt

# cut -b 2,-3,4 testfiles/hello3.txt

# cut -b -3,5- testfiles/hello3.txt

# cut -b -3,3- testfiles/hello3.txt

# cut -b 1-,-2 testfiles/hello3.txt
