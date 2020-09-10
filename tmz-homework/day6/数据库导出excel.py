import pymysql
import traceback
import xlwt

cur = ''
x = ''


# 操作数据库
def connect_mysql(s):
    global cur, x
    connect = pymysql.connect(host='118.24.3.40',
                              user='jxz',
                              password='123456',
                              db='jxz',
                              port=3306,
                              autocommit=True
                              )
    # noinspection PyBroadException
    # 不管操作数据库是否报错，都要关闭数据库
    try:
        cur = connect.cursor(pymysql.cursors.DictCursor)
        cur.execute(s)
        x = cur.fetchall()
    except BaseException:
        print('错误信息：', traceback.format_exc())
    finally:
        cur.close()
        connect.close()
    return x


# 写入到excel
def export_excel():
    table_name = input('请输入您要查询的表名：').strip()
    result = connect_mysql('select * from %s;' % table_name)
    if result:
        # 获取表头
        table_header = [dict_key for dict_key in result[0]]
        # 获表数据
        table_list = []
        for i in result:
            table_data = [i[dict_key] for dict_key in i]
            table_list.append(table_data)
        table_list.insert(0, table_header)  # 插入表头
        book = xlwt.Workbook()
        sheet = book.add_sheet('sheet1')
        for row, data in enumerate(table_list):  # 控制行
            for col, s in enumerate(data):  # 控制列
                sheet.write(row, col, s)
        book.save('%s.xlsx' % table_name)
    else:
        print('数据为空或者表不存在')


export_excel()
