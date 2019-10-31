# SecurityRambler
一个瞎鸡儿乱打EXP的辣鸡爬虫,顺带加上指纹识别

如果有自己的0day或者新公开的1day，可以快速更具历史指纹整活


## 关于

只做检测，不做GetShell

不想自己写，一个爬虫+各种exp缝合下

做个快乐的缝合怪

## 使用

### 库

  - peewee （我才不想自己写sql）
  - requests （优雅的HTTP轮子
  

## TODO：瞎鸡儿打啥EXP?

  - Weblogic 
  - Struct2 
  - Thinkphp 等
  - PhpStudy 后门
  - Nginx+php-fpm 漏洞
  - Spring 等
  
## 实现
鸭子类型 嘎嘎嘎。只要符合调用规定就能调用
```python
def _exploit(target):return True 
```

# 参考

  - [REC任意代码执行漏洞大全](Other/RCE漏洞执行大全.pdf)
  - [WTF_SCAN](https://github.com/dyboy2017/WTF_Scan)