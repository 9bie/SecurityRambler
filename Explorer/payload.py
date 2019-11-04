import importlib
import glob
from pathlib import Path
import queue
from config import *
from .database import write_exploit


class Exploit:

    def __init__(self):
        self.list = queue.Queue(5000)
        self.plugin_center = {}
        for i in glob.glob("../Exploit/*.py"):
            try:
                obj = importlib.import_module(f"..Exploit.{Path(i).stem}")
                register, plugins = obj.initialization()
                self.plugin_center[register] = plugins
            except:
                print("Load Plugin Failed: %s" % Path(i).stem)

    def add(self, target):
        self.list.put(target, block=True)

    def start(self):
        while 1:
            target = self.list.get(block=True)
            for i in self.plugin_center:
                name, result = self.plugin_center[i]["callback"](target)
                if result:
                    write_exploit(target, name)
                    if Just_One:
                        break
