#coding=utf-8
import pymysql
import threading
from datetime import datetime

def sfzh_sql_insert():
    conn = pymysql.connect(host='localhost', user='root', password="123456",
                           database='chs', port=3306,
                           charset='utf8')
    cus= conn.cursor()
    #id = int(id)
    try:
        for i in range(10000):
            sql = ("insert into app_user2(`name`,`email`,`phone`,`gender`,`password`,`age`)VALUES(CONCAT('user',('%s')),'12345678@polyu.com',CONCAT('18',FLOOR(RAND()*(999999999-100000000)+100000000)),FLOOR(RAND()*2),UUID(),FLOOR(RAND()*100))")%(i)
            #tlock.acquire()
            cus.execute(sql)
            conn.commit()
            #tlock.release()
    except Exception as e:
        print ("one error happen",e)
    finally:
        cus.close()
        conn.close()


class myThread(threading.Thread):
    def __init__(self,id):
        threading.Thread.__init__(self)
        self.id = id
        pass
    def run(self):
        sfzh_sql_insert()
        #print ("开始操作%s"%i)

if __name__ == '__main__':
    tik = datetime.now()
    sfzh_sql_insert()
    tok = datetime.now()
    timecos = format((tok - tik).seconds)
    print('total time cost:\t',timecos)
