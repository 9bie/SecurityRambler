# coding:utf-8
import Explorer

b = Explorer.Exploit()
a = Explorer.Spider(b.add)
a.add("https://www.hao123.com")
a.start()
