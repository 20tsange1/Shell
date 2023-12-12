import tempfile
import unittest
import os
from pathlib import Path
from apps.pwd import Pwd


class TestPwd(unittest.TestCase):
    @classmethod
    def setup(self):
        self.test_dir = tempfile.TemporaryDirectory()
        self.temp_path = Path(self.test_dir.name)
        os.chdir(self.temp_path)
        return []

    @classmethod
    def teardown(self):
        self.test_dir.cleanup()

    def test_pwd(self):
        out = self.setup()
        Pwd().execute([], out)
        self.assertEqual(str(self.temp_path) + "\n", "".join(out))
        self.teardown()

    def test_pwd_root(self):
        out = self.setup()
        os.chdir("/")
        Pwd().execute([], out)
        self.assertEqual("/\n", "".join(out))
        self.teardown()
