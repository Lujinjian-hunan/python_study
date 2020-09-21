import pymysql,xlwt
import traceback,hashlib
MYSQL_INFO = {
    'host':'118.24.3.40',
    'user':'jxz',
    'password':'123456',
    'db':'jxz',
    'charset':'utf8',
    'autocommit':True
}

def execute_sql(sql):
    conn = pymysql.connect(**MYSQL_INFO) #xx=xxx,xx=xx,
    cur = conn.cursor(pymysql.cursors.DictCursor)
    try:
        cur.execute(sql)
    except:
        print('sql不正确')
        traceback.print_exc()
    else:
        return cur.fetchall() #None  []
    finally:
        conn.close()
        cur.close()

def write_excel(name,data):
    book = xlwt.Workbook()
    sheet = book.add_sheet('sheet1')
    for index, key in enumerate(data[0]):  # 写表头
        sheet.write(0, index, key)
    for row, item in enumerate(data, 1):  # 写数据
        for col, value in enumerate(item.values()):
            sheet.write(row, col, value)

    book.save(name + '.xls')


def my_md5(s):
    s = str(s)
    s = s.encode()
    m = hashlib.md5(s)  # bytes,不可逆
    result = m.hexdigest()
    return result