import pymysql
import traceback

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
        cur = connect.cursor()
        cur.execute(s)
        x = cur.fetchall()
    except BaseException:
        print('错误信息：', traceback.format_exc())
    finally:
        cur.close()
        connect.close()
    return x


# 判断价格
def is_price(s):
    s = str(s)
    if s.count('.') == 1:
        left, right = s.split('.')
        if left.isdigit() and right.isdigit():
            return float(s)
    elif s.isdigit():
        if int(s) > 0:
            return int(s)
    else:
        print('价格必须是大于0的数字')
        return False


# 判断数量
def is_count(s):
    s = str(s)
    if s.isdigit():
        if int(s) > 0:
            return int(s)
    else:
        print('数量必须是大于0的整数')
        return False


# 查询商品
def select():
    com_name = input('请输入您要查询的商品名称，输入all 查询所有商品：').strip()
    # 判断输入是否为空
    if com_name:
        if com_name == 'all':
            result = connect_mysql('select * from tmz_ljj_commodity;')
        else:
            result = connect_mysql("select * from tmz_ljj_commodity where trade_name='%s';" % com_name)
        # 判断查询到的结果是否为空，不为空输出结果
        if result:
            # 将查询到的数组中价格的类型转为float
            for i in result:
                data = [j for j in i]
                data[-1] = float(data[-1])
                print(data)
        else:
            print('查询的商品不存在')
    else:
        print('输入不能为空')


# 新增商品
def add():
    com_name = input('请输入您要新增的商品名称：').strip()
    price = input('请输入商品价格：').strip()
    count = input('请输入商品数量：').strip()
    # 判断输入是否为空
    if com_name and price and count:
        # 先查询商品是否存在，不存在才能去数据库新增商品
        result = connect_mysql("select count(*) from tmz_ljj_commodity where trade_name='%s';" % com_name)
        if not result[0][0]:
            # 判断价格和数量是否符合规则
            if is_price(price) and is_count(count):
                connect_mysql("insert into tmz_ljj_commodity(trade_name, count, price) "
                              "values ('{}', '{}', '{}');".format(com_name, count, price))
                print('新增成功')
        else:
            print('商品已存在')
    else:
        print('输入不能为空')


# 修改商品
def update():
    com_name = input('请输入您要修改的商品名称：').strip()
    # 判断输入是否为空
    if com_name:
        # 先查询商品是否存在，存在则修改商品的信息
        result = connect_mysql("select count(*) from tmz_ljj_commodity where trade_name='%s';" % com_name)
        if result[0][0]:
            new_price = input('请输入修改后的商品价格：').strip()
            new_count = input('请输入修改后的商品数量：').strip()
            # 判断价格和数量是否符合规则
            if is_price(new_price) and is_count(new_count):
                connect_mysql("update tmz_ljj_commodity set count = '{}', price = '{}' "
                              "where trade_name = '{}';".format(new_count, new_price, com_name))
            print('修改成功')
        else:
            print('您输入的商品不存在')
    else:
        print('输入不能为空')


# 删除商品
def delete():
    com_name = input('请输入您要删除的商品名称：').strip()
    # 判断输入是否为空
    if com_name:
        # 先查询商品是否存在，存在才能删除商品
        result = connect_mysql("select count(*) from tmz_ljj_commodity where trade_name='%s';" % com_name)
        if result[0][0]:
            connect_mysql("delete from tmz_ljj_commodity where trade_name='%s'" % com_name)
            print('删除成功')
        else:
            print('您输入的商品不存在')
    else:
        print('输入不能为空')


choice = input('请输入您的选择(1、查看商品 2、新增商品 3、修改商品 4、删除商品)：').strip()
d = {'1': select, '2': add, '3': update, '4': delete}


def your_choice(c):
    if c in d:
        return d[c]()
    else:
        print('请输入正确的操作!')


your_choice(choice)
