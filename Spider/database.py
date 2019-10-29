from peewee import *
from config import *
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
