import tempfile
import unittest
from pathlib import Path
from apps.uniq import Uniq
from application import Application
from unsafe_decorator import UnsafeDecorator
from application_factory import ApplicationFactory
from error import ApplicationError

class TestUnsafe(unittest.TestCase):
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

    def test_unsafe_uniq(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        UnsafeDecorator(Uniq()).execute([self.test_file[0]], out)
        self.assertEqual("".join(out), "AAA\nBBB\nCCC\n")
        self.teardown()

    def test_unsafe_uniq_throw(self):
        out = self.setup(["AAA\nAAA\nBBB\nBBB\nCCC\nCCC\n"])
        UnsafeDecorator(Uniq()).execute(["-c", self.test_file[0]], out)
        self.assertEqual(
            "".join(out),
            "An exception occurred: Wrong flags [uniq -i <file>?]\n",
        )
        self.teardown()

    def test_safe_apps(self):
        self.setup([])
        self.assertEqual(
            len(ApplicationFactory(unsafe=False).application_map), 23
        )
        self.teardown()

    def test_unsafe_apps(self):
        self.setup([])
        self.assertEqual(len(ApplicationFactory().application_map), 46)
        self.teardown()