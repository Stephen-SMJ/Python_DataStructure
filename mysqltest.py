import pymysql
import threading
from datetime import datetime

class query_Mysql():

    def __init__(self, host, user, pw, db, port):
        self.result = ''
        self.host = host
        self.user = user
        self.pw = pw
        self.db = db
        self.port = port
        self.timecos = ''
        try:
            conn = pymysql.connect(host=self.host, user=self.user, password=self.pw,
                                   database=self.db, port=self.port,
                                   charset='utf8')
            self.conn = conn
            self.cus = conn.cursor()
        except pymysql.MySQLError as e:
            self.result = e


    def query(self, sql):
        cus = self.cus
        tik = datetime.now()
        cus.execute(sql)
        tok = datetime.now()
        self.timecos = format((tok - tik).seconds)
        self.result = cus.fetchall()
        self.cus.close()
        self.conn.close()


if __name__ == '__main__':
    con = query_Mysql(host='localhost', user='root', pw="123456", db='chs', port=3306)
    sql_String = "select * from app_user where phone = '18747046298'"
    con.query(sql_String)
    print(con.result)
    print(con.timecos)
