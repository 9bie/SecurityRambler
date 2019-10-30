from peewee import *
from config import *
from datetime import datetime
import json

db = SqliteDatabase("test.db") if not IS_MYSQL else MySQLDatabase(host=MYSQL_HOST, database=MYSQL_DATABASE,
                                                                  user=MYSQL_USERNAME, password=MYSQL_PASSWD, port=3306)


class BaseModel(Model):
    class Meta:
        database = db

    def __str__(self):
        r = {}
        for k in self.__data__.keys():
            try:
                r[k] = str(getattr(self, k))
            except:
                r[k] = json.dumps(getattr(self, k))
        # return str(r)
        return json.dumps(r, ensure_ascii=False)


class Exploit(BaseModel):
    id = PrimaryKeyField()
    status = BooleanField(default=False)
    domain = TextField()
    target = TextField()
    payload = TextField()
    update_time = DateTimeField(default=datetime.now)


class Spider(BaseModel):
    id = PrimaryKeyField()
    status = BooleanField(default=False)
    domain = TextField()
    target = TextField()
    title = TextField()
    update_time = DateTimeField(default=datetime.now)


Spider.create_table()


# class SubSpider:
#     main = ForeignKeyField(Explorer, "sub")
#     Other = TextField()
#     title = TextField()


def select_spider(target: str):
    data = Spider.select().where(Spider.target == target)
    if len(data) != 0:
        return True
    else:
        return False


def select_exploit(target: str):
    return False


def write_spider(status: bool, domain: str, target: str, title: str):
    print("Write on Db\n\tDomain: %s\n\tUrl: %s\n\tTitle: %s" % (domain, target, title))
    Spider.create(status=status, domain=domain, target=target, title=title)


def write_exploit_result(status: bool, target: str, cve: str):
    if status:
        pass
