from unsafe_decorator import UnsafeDecorator
from apps.pwd import Pwd
from apps.cd import Cd
from apps.echo import Echo
from apps.ls import Ls
from apps.cat import Cat
from apps.head import Head
from apps.tail import Tail
from apps.grep import Grep
from apps.sort import Sort
from apps.cut import Cut
from apps.find import Find
from apps.uniq import Uniq
from apps.mkdir import Mkdir
from apps.touch import Touch
from apps.rm import Rm
from apps.rmdir import Rmdir
from apps.mv import Mv
from apps.cp import Cp
from apps.color import Color
from apps.font import Font
from apps.sed import Sed
from apps.wc import Wc
from apps.exit import Exit


class ApplicationFactory:
    def __init__(self, unsafe=True):
        self.application_map = {
            "pwd": Pwd(),
            "cd": Cd(),
            "echo": Echo(),
            "ls": Ls(),
            "cat": Cat(),
            "head": Head(),
            "tail": Tail(),
            "grep": Grep(),
            "sort": Sort(),
            "cut": Cut(),
            "find": Find(),
            "uniq": Uniq(),
            "mkdir": Mkdir(),
            "touch": Touch(),
            "rm": Rm(),
            "rmdir": Rmdir(),
            "mv": Mv(),
            "cp": Cp(),
            "color": Color(),
            "font": Font(),
            "sed": Sed(),
            "wc": Wc(),
            "exit": Exit(),
        }
        # add unsafe commands to map
        if unsafe:
            self.add_unsafe_applications()

    def add_unsafe_applications(self):
        unsafe = {}
        for name, app in self.application_map.items():
            unsafe[f"_{name}"] = UnsafeDecorator(app)
        self.application_map.update(unsafe)
