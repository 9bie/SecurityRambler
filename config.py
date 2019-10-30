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
Search_Engine_Mode = True
'''
SearchEngineMode：
    是否保存全部子页面网页，这会导致数据库变得极大。如果你不是想做一个搜索引擎，不推荐这样做
'''

# Exploit
Used = []
'''
Used:
  为空则默认引用Exploit下全部，否则只引用List内的文件
'''
Test_All_Page = False
'''
Test_All_Page:
    如果Search_Engine_Mode为True，将会攻击所有Search_Engine_Mode模式下爬取的页面
'''