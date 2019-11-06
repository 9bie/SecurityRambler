# SecurityRambler
一个瞎鸡儿乱打EXP的辣鸡爬虫,顺带加上指纹识别

如果有自己的0day或者新公开的1day，可以快速更具历史指纹整活


## 关于

只做检测，不做GetShell

不想自己写，一个爬虫+各种exp缝合下

做个快乐的缝合怪。

请注意，在目前版本

该工具并不是一款cms识别工具，或者什么精准exp自动选择攻击工具

而是一款模糊，批量，专门探测互联网上隐藏的，难以检测的工具。

针对目标是那些没有指纹的站点。

推荐Exploit那些添加一些危害性高的，比如前段时间的nginx+php-fpm 利用或者其他的一些任意代码执行的EXP。

也许在后续版本会完善功能。

为了控制爬虫速度，请尽量选择近两年内，高危，无特征的exploit。

年代久远的漏洞是*没有什么意义的*，成本与回报不成正比，除非你能很确定的*该漏洞广泛存在并且未被修复*

## 使用

### 库

  - peewee （我才不想自己写sql）
  - requests （优雅的HTTP轮子
  - gevent

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

### 插件规则
以下为 `Exploit/CVE-XXXX-XXX.py.example`节选
```python
def check(url):
    '''
    检测函数，url必要的
    :param url:
    :return:
    '''
    return False


def initialization():
    '''
    必要函数，作为插件初始化用
    :return: 返回漏洞名称和插件调用信息
    '''
    return "TestFunction", {
        "callback": check,  # 必要指向参数为url的检测函数
    }

```

# 参考

  - [REC任意代码执行漏洞大全](Other/RCE漏洞执行大全.pdf)
  - [WTF_SCAN](https://github.com/dyboy2017/WTF_Scan)
  - [AutoFuck](https://github.com/harry1080/AutoFuck)