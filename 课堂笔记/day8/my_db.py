import pymysql
from loguru import logger
import traceback

MYSQL_INFO = {
    'host':'118.24.3.40',
    'user':'jxz',
    'password':'123456',
    'db':'jxz',
    'charset':'utf8',
    'autocommit':True
}
class MySQL:
    def __init__(self,host,user,password,db,charset='utf8',autocommit=True):
        self.conn = pymysql.connect(user=user,host=host,password=password,db=db,charset=charset,autocommit=autocommit)
        self.cursor = self.conn.cursor()


    def __del__(self):
        self.__close()

    def execute(self,sql):
        try:
            self.cursor.execute(sql)
        except Exception:
            logger.error('sql执行出错，sql语句是{}',sql)
            logger.error(traceback.format_exc())

    def fetchall(self,sql):
        self.execute(sql)
        return self.cursor.fetchall()

    def fetchone(self,sql):
        self.execute(sql)
        return self.cursor.fetchone()

    def bak_db(self):
        pass

    def __close(self):
        self.cursor.close()
        self.conn.close()

if __name__ == '__main__':
    my = MySQL(**MYSQL_INFO)
    print(my.fetchall('select * from app_myuser;'))
    my.fetchone('select * from app_myuser where id=1;')
    my.fetchone('select * from app_myuser where id=1;')
    my.fetchone('select * from app_myuser where id=1;')




