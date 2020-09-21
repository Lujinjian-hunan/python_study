import pymysql,xlwt
import traceback,hashlib

import redis
from loguru import logger


import sys


logger.remove()  # 清除它的默认设置设置
fmt = '[{time}][{level}][{file.path}:line:{line}:function_name:{function}] ||msg={message}'
# level file function module time message
logger.add(sys.stdout, level='INFO', format=fmt)  # 咱们本地运行的时候，在控制台打印
# logger.add('wxl.log',level='DEBUG',format=fmt,encoding='utf-8',enqueue=True,rotation='1 s',retention='10 seconds')#写在日志文件里面
logger.add('wxl.log', level='DEBUG', format=fmt, encoding='utf-8', enqueue=True, rotation='1 day',
           retention='10 days')  # 写在日志文件里面

MYSQL_INFO = {
    'host':'118.24.3.40',
    'user':'jxz',
    'password':'123456',
    'db':'jxz',
    'charset':'utf8',
    'autocommit':True
}



REDIS_INFO = {
    'host':'118.24.3.40',
    'password':'HK139bc&*',
    'db':0,
    'port':6379,
    'decode_responses':True
}

def execute_sql(sql,more=False):
    conn = pymysql.connect(**MYSQL_INFO) #xx=xxx,xx=xx,
    cur = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
    except:
        logger.error('sql错误，{}',traceback.format_exc())
    else:
        if more:
            return cur.fetchall() #None  [{} ]
        return cur.fetchone()  #{'xx':'xx'}
    finally:
        conn.close()
        cur.close()

class Tool:

    @staticmethod
    def write_excel(name,data):
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        for index, key in enumerate(data[0]):  # 写表头
            sheet.write(0, index, key)
        for row, item in enumerate(data, 1):  # 写数据
            for col, value in enumerate(item.values()):
                sheet.write(row, col, value)

        book.save(name + '.xls')

    @staticmethod
    def my_md5(s):
        s = str(s)
        s = s.encode()
        m = hashlib.md5(s)  # bytes,不可逆
        result = m.hexdigest()
        return result

def redis_str(key,value=False,expire_time=None):
    r = redis.Redis(**REDIS_INFO)
    if value:
        r.set(key,value,expire_time)
    else:
        return r.get(key)

def redis_hash():
    pass

def check_session(session_id):
    result = redis_str(session_id)
    if result:
        return result
    return False



