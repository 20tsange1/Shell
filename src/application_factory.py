from unsafe_decorator import UnsafeDecorator
from help_decorator import HelpDecorator
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
from apps.help import Help


class ApplicationFactory:
    def __init__(self, helpful=True, unsafe=True):
        self.application_map = {
            "cat": Cat(),
            "cd": Cd(),
            "color": Color(),
            "cp": Cp(),
            "cut": Cut(),
            "echo": Echo(),
            "exit": Exit(),
            "find": Find(),
            "font": Font(),
            "grep": Grep(),
            "head": Head(),
            "ls": Ls(),
            "mkdir": Mkdir(),
            "mv": Mv(),
            "pwd": Pwd(),
            "remove": Rm(),
            "rmdir": Rmdir(),
            "sed": Sed(),
            "sort": Sort(),
            "tail": Tail(),
            "touch": Touch(),
            "uniq": Uniq(),
            "wc": Wc(),
        }
        # add unsafe commands to map
        if helpful:
            self.add_helpful_applications()
        if unsafe:
            self.add_unsafe_applications()

    def add_unsafe_applications(self):
        unsafe = {}
        for name, app in self.application_map.items():
            unsafe[f"_{name}"] = UnsafeDecorator(app)
        self.application_map.update(unsafe)
    
    def add_helpful_applications(self):
        for name in self.application_map.keys():
            self.application_map[name] = HelpDecorator(self.application_map[name])
        self.application_map["help"] = Help()
