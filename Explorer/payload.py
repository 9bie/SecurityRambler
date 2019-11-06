# coding: utf-8
import importlib
import glob
from pathlib import Path
import queue
from config import *
from .database import write_exploit
import requests
from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED, as_completed


class Exploit:

    def __init__(self):
        self.list = queue.Queue(5000)
        self.plugin_center = {}
        self.executor = ThreadPoolExecutor(max_workers=MAX_THREAD_EXPLOIT)
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
            response = requests.get(target, headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
                'Referer': target,
                'robot': "SecurityExplorer"

            })
            server = response.headers.get("Server")
            x_powered_by = response.headers.get("X-Powered-By")
            # for i in self.plugin_center:
            # name, result = self.plugin_center[i]["callback"](target)
            # todo: 指纹识别
            all_task = [self.executor.submit(self.plugin_center[i]["callback"], target) for i in self.plugin_center]
            for future in as_completed(all_task):
                name, result = future.result()
                if result:
                    write_exploit(target, name)
                    # if Just_One:
                    #     break
