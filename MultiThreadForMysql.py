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

    def inset_mock(self):
        try:
            for i in range(100000):
                sql = ("insert into app_user2(`name`,`email`,`phone`,`gender`,`password`,`age`)VALUES(CONCAT('user',('%s')),'12345678@polyu.com',CONCAT('18',FLOOR(RAND()*(999999999-100000000)+100000000)),FLOOR(RAND()*2),UUID(),FLOOR(RAND()*100))") % (i)
                # tlock.acquire()
                self.cus.execute(sql)
                self.conn.commit()
                # tlock.release()
        except Exception as e:
            print("one error happen", e)
        finally:
            self.cus.close()
            self.conn.close()


class Mythread(threading.Thread, query_Mysql):
    def __init__(self, host, user, pw, db, port, id):
        threading.Thread.__init__(self)
        query_Mysql.__init__(self, host, user, pw, db, port)
        self.id = id
        self.timecos = 0
        pass

    def run(self):
        # print('thread' + str(self.id) + 'start')
        query_Mysql(self.host, self.user, self.pw, self.db, self.port)
        tik = datetime.now()
        query_Mysql.inset_mock(self)
        tok = datetime.now()
        self.timecos = format((tok - tik).seconds)

if __name__ == '__main__':
    threads = []
    cos = []
    tlock = threading.Lock()
    for i in range(100):
        thread = Mythread(host='localhost', user='root', pw="123456", db='chs', port=3306, id=i)
        threads.append(thread)
    for i in range(len(threads)):
        threads[i].start()
    [j.join() for j in threads]
    for i in threads:
        cos.append(i.timecos)
    tcos = sum(cos)
    print('total time cost:\t',tcos)
