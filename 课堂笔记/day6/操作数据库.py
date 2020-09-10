import pymysql
# oracle sqlserver

# 118.24.3.40
# jxz user
# 123456 password
# jxz db

host = '118.24.3.40'
user = 'jxz'
password = '123456'  # str类型
db = 'jxz'
port = 3306  #int类型

connect = pymysql.connect(host=host,
                user=user,
                password=password,
                db=db,
                port=port,
                autocommit=True  # 自动提交
                )
# cur = connect.cursor()  # 建立游标，仓库管理员
cur = connect.cursor(pymysql.cursors.DictCursor)  # 以字典形式
# cur.execute('insert into students (name,class) values ("张三","天马座");')
# cur.execute('insert into students (id,name,sex,age,class,addr) values (60,"张三","男","20","天马座","北京");')
# cur.execute('delete from students where id=50 ;')
cur.execute('select * from students limit 5;')  # 写sql语句
# print('fetchone', cur.fetchone())
# print('fetchmany', cur.fetchmany(2))
print('fetchall', cur.fetchall())  # 拿到所有的结果，二维数组

# for data in cur:
#     print(data)
# print(cur)


# connect.rollback()  # 回滚
# connect.commit()  # 提交
# print(cur.description)  # 表的描述
cur.close()
connect.close()