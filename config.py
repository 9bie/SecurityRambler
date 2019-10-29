#coding:utf-8

# DataBase
MYSQL_HOST = ''
MYSQL_PORT = ''
MYSQL_USERNAME = ''
MYSQL_PASSWD = ''

# Spider
Customize_UserAgent = ''
THREAD = True

MAX_THREAD = 10

Full_Spider2OtherLink = False 
'''
Full_Spider2OtherLink:
  为True这项将会抓取所有页面，否则只会抓取首页下的连接
'''

# Exploit
Used = []
'''
Used:
  为空则默认引用Exploit下全部，否则只引用List内的文件
'''