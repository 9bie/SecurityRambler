# coding:utf-8

# DataBase
IS_MYSQL = True
MYSQL_HOST = 'localhost'
MYSQL_PORT = '3389'
MYSQL_DATABASE = 'Security'
MYSQL_USERNAME = 'root'
MYSQL_PASSWD = 'bakabie'

# Explorer
Customize_UserAgent = ''
THREAD = True


MAX_THREAD = 10
'''
MAX_THREAD:
    并发数量
'''

Full_Spider2OtherLink = False
'''
Full_Spider2OtherLink:
  为True这项将会抓取所有页面，否则只会抓取首页下的连接
'''

Just_One = True
'''
Just_One:
    发现漏洞就停止，节省时间，默认开启
'''

Search_Engine_Mode = True
'''
SearchEngineMode：
    是否保存爬取子页面网页。
'''

# Exploit
Used = []
'''
Used:
  为空则默认引用Exploit下全部，否则只引用List内的文件
'''

CMS_Engine = False
'''
CMS_Engine:
    CMS检测引擎，如果你的EXP库不是特别的多，那么不推荐打开这个
'''