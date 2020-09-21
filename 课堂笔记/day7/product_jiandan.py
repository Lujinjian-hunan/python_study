import tools
def read_products():
    sql = 'select * from tmz_ljj_commodity;'
    data = tools.execute_sql(sql)
    #[{'id':1,'trade_name':'xxx','count':xx,'price':xx}, {'id':1,'trade_name':'xxx','count':xx,'price':xx}]
    d = {}
    for item in data:
        name = item.get('trade_name')
        count = item.get('count')
        price = float(item.get('price'))
        d[name] = {'count':count,'price':price}
    return d



def write_products(data):

    truncate_sql = 'truncate table tmz_ljj_commodity;'
    tools.execute_sql(truncate_sql)

    for k,value in data.items():
        count = value.get('count')
        price = value.get('price')
        insert_sql = 'insert into tmz_ljj_commodity (trade_name,count,price) ' \
                     'values ("%s",%s,%s);' %(k,count,price)
        tools.execute_sql(insert_sql)


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
        products = read_products()
        if product_name == 'all':
            print(products)
        elif product_name not in products:
            print('商品不存在')
        else:
            product = products.get(product_name)
            print('商品信息:', product)
    else:
        print('不能为空')

def add_product():
    product_name = input('请输入商品名称:').strip()
    price = input('请输入商品价格:').strip()
    count = input('请输入商品数量:').strip()
    if product_name and price and count:
        if is_price(price) and is_digit(count):
            products = read_products()
            if product_name not in products:
                products[product_name] = {"count":count,"price":price}
                write_products(products)
                'insert into '
                print('商品新增成功！')
            else:
                print('商品已经存在')
        else:
            print('价格/数量不合法')
    else:
        print('不能为空')


def modify_product():
    product_name = input('请输入商品名称:').strip()
    # new_product_name = input('请输入新的商品名称:').strip()
    price = input('请输入商品价格:').strip()
    count = input('请输入商品数量:').strip()
    if product_name and price and count:
        if is_price(price) and is_digit(count):
            products = read_products()
            if product_name in products:
                # products.pop(product_name)
                products[product_name] = {"count":count,"price":price}
                # products[new_product_name] = {"count":count,"price":price}
                write_products(products)
                print('商品修改成功！')
            else:
                print('商品不存在')
        else:
            print('价格/数量不合法')
    else:
        print('不能为空')


def delete_product():
    product_name = input('请输入商品名称:').strip()
    if product_name:
        products = read_products()
        if product_name not in products:
            print('商品不存在')
        else:
            products.pop(product_name)
            write_products(products)

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