import tools

def get_single_product(name):
    sql = 'select * from tmz_ljj_commodity where trade_name = "%s";' % name
    return tools.execute_sql(sql)

def is_digit(number):
    s = str(number)
    if s.isdigit():
        if int(s) > 0:
            return True

def is_price(price):  #>0的整数和小数都可以 #1.7
    s = str(price)
    if is_digit(s):
        return True
    else:
        if s.count('.') == 1:  # 1.3
            left, right = s.split('.')
            if left.isdigit() and right.isdigit():  # 正小数 #0.0
                if float(s)>0:
                    return True

def show_product():
    product_name = input('请输入商品名称:').strip()
    if product_name:
        if product_name == 'all':
            sql = 'select * from tmz_ljj_commodity;'
            print(tools.execute_sql(sql))
        else:
            product = get_single_product(product_name)
            if product:
                print('商品信息：',product)
            else:
                print('你输入的商品不存在')
    else:
        print('不能为空')

def add_product():
    product_name = input('请输入商品名称:').strip()
    price = input('请输入商品价格:').strip()
    count = input('请输入商品数量:').strip()
    if product_name and price and count:
        if is_price(price) and is_digit(count):
            if get_single_product(product_name):
                print('商品已经存在')
            else:
                insert_sql = 'insert into tmz_ljj_commodity (trade_name,count,price) ' \
                             'values ("%s",%s,%s);' % (product_name, count, price)
                tools.execute_sql(insert_sql)
                print('商品新增成功！')

        else:
            print('价格/数量不合法')
    else:
        print('不能为空')


def modify_product():
    product_name = input('请输入商品名称:').strip()
    price = input('请输入商品价格:').strip()
    count = input('请输入商品数量:').strip()
    if product_name and price and count:
        if is_price(price) and is_digit(count):
            if get_single_product(product_name):
                sql = 'update tmz_ljj_commodity set price=%s,count=%s where trade_name="%s";' %(
                    price,count,product_name
                )
                tools.execute_sql(sql)
                print('商品修改成功')
            else:
                print('商品不存在')
        else:
            print('价格/数量不合法')
    else:
        print('不能为空')


def delete_product():
    product_name = input('请输入商品名称:').strip()
    if product_name:
        if get_single_product(product_name):
            sql='delete from tmz_ljj_commodity where trade_name="%s"; ' % product_name
            tools.execute_sql(sql)
            print('商品已删除')
        else:
            print('商品不存在')
    else:
        print('不能为空')


choice = input('1、查看商品 2、新增 3、修改  4、删除： ')

func_map = {'1':show_product,'2':add_product,'3':modify_product,'4':delete_product}
if choice in func_map:
    func_map[choice]()
else:
    print('请输入正确的选项！')

# if choice == '1':
#     show_product()
# elif choice == '2':
#     add_product()