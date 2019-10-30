from concurrent.futures import ThreadPoolExecutor, wait, FIRST_COMPLETED
from config import *
import requests
import queue
from .database import write_spider, select_spider
from urllib.parse import urlparse
import re


class Parser:
    def __init__(self, control, exploit,target):
        self.target = target
        self.control = control
        self.exploit = exploit
        self.parser_list = []
        self.url = urlparse(self.target)

    def parser(self):
        if select_spider(self.target):
            return
        response = requests.get(self.target, headers={
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
            'Referer': self.url.netloc,
            'robot': "SecurityExplorer",
        })
        if response.status_code != 200:
            write_spider(False, self.url.netloc, self.target, "")
            return
        text = response.text
        title = re.findall(r'<title>.*?</title>', text)
        if title:
            title = title[0][len("<title>"):len(title) - len("</title>") - 1]
        regular = re.compile(r'<.*?(href=".*?").*?')
        url = re.findall(regular, text)
        clean = []
        for i in url:
            i = i[6:len(i) - 1]
            c = re.findall(r'https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', i)
            if len(c) != 0:
                if Search_Engine_Mode:
                    clean.append(i)
                else:
                    clean.append(c[0])
        clean = list(set(clean))
        for z in clean:
            self.control(z)
        write_spider(True, self.url.netloc, self.target, title)


class Exploit:
    def __init__(self):
        self.list = queue.Queue(500)

    def add(self, target):
        self.list.put(target, block=True)

    def start(self):
        while 1:
            pass


class Spider:

    def __init__(self, callback):
        self.list = queue.Queue()
        self.executor = None
        self.callback = callback

    def add(self, target):
        self.list.put(target)

    def start(self):
        self.executor = ThreadPoolExecutor(max_workers=(MAX_THREAD if not IS_MYSQL else 1))
        while 1:
            target = self.list.get(block=True)
            parser = Parser(self.add, target, self.callback)
            # result =
            self.executor.submit(parser.parser())
            # wait([result], return_when=FIRST_COMPLETED)
