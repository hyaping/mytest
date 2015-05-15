#-*- coding:utf-8 -*-

import pymysql

class DBHelper(object):
    def __init__(self,host,user,passwd,db,charset="utf8"):
        self._host = host
        self._user = user
        self._passwd = passwd
        self._db = db
        self._charset = charset
        self._conn = pymysql.connect(host = self._host,
            user = self._user,passwd = self._passwd,db = self._db,
            charset = self._charset)

    def close(self):
        self._conn.close()

    def execute(self,sql):
        curs = self._conn.cursor()
        result = curs.execute(sql)
        self._conn.commit()
        curs.close()
        return result

    def query(self,sql):
        curs = self._conn.cursor()
        curs.execute(sql)
        result =  [i for i in curs]
        curs.close()
        return result


print "__name__:",__name__

if __name__ == '__main__':
     params = {"host" : "localhost", "user" : "root",
               "passwd" : "", "db" : "db1"}   #字典
     dbhelper = DBHelper(**params)
     print dbhelper.query("SELECT * FROM tweb")
     print "=" * 80
     print dbhelper.query("SELECT * FROM tweb WHERE id = 20")
     dbhelper.close()
