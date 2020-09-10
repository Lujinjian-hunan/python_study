import json


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
        print('价格必须是大于0的数值')
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


# 读取文件
def read_file():
    with open('a.json', encoding='utf-8') as fr:
        return json.load(fr)


# 写入文件
def write_file(result):
    with open('a.json', 'w', encoding='utf-8') as fw:
        json.dump(result, fw, ensure_ascii=False, indent=4,)


# 查询商品
def select():
    com = input('请输入您要查询的商品名称，输入all 查询所有商品：').strip()
    if com:
        if com in read_file():
            print(read_file()[com])
        elif com == 'all':
            print(read_file())
        else:
            print('您输入的商品不存在')
    else:
        print('输入不能为空')


# 新增商品
def add():
    com_name = input('请输入您要新增的商品名称：').strip()
    price = input('请输入商品价格：').strip()
    count = input('请输入商品数量：').strip()
    if com_name and price and count:
        result = read_file()
        if com_name in result:
            print('该商品已存在')
        # 调用判断价格和数量的函数来判断输入的价格和数量是否正确，正确则重新赋值
        elif is_price(price) and is_count(count):
            count, price = is_count(count), is_price(price)
            # 把新增的商品写入字典，在写入文件中
            result[com_name] = {'count': count, 'price': price}
            write_file(result)
            print('新增成功')
    else:
        print('输入不能为空')


# 修改商品
def update():
    com_name = input('请输入您要修改的商品名称：').strip()
    result = read_file()
    if com_name:
        if com_name in result:
            confirm = input('请问是否要修改商品名称(1、是 2、否)：').strip()
            if confirm:
                if confirm == '1':
                    if com_name in result:
                        new_com_name = input('请输入修改后的商品名称：').strip()
                        new_price = input('请输入修改后的商品价格：').strip()
                        new_count = input('请输入修改后的商品数量：').strip()
                        if new_com_name in result:
                            print('该商品名已存在')
                        elif new_com_name and new_price and new_count:
                            # 调用判断价格和数量的函数来判断输入的价格和数量是否正确，正确则重新赋值
                            if is_price(new_price) and is_count(new_count):
                                new_count, new_price = is_count(new_count), is_price(new_price)
                                # 把修改的商品写入字典，删除原来的数据并将修改后的商品写入文件中
                                result.pop(com_name)
                                result[new_com_name] = {'count': new_count, 'price': new_price}
                                write_file(result)
                                print('修改成功')
                        else:
                            print('输入不能为空')
                elif confirm == '2':
                    if com_name in result:
                        new_price = input('请输入修改后的商品价格：').strip()
                        new_count = input('请输入修改后的商品数量：').strip()
                        if new_price and new_count:
                            if is_price(new_price) and is_count(new_count):
                                result[com_name] = {'count': new_count, 'price': new_price}
                                write_file(result)
                                print('修改成功')
                        else:
                            print('输入不能为空')
                else:
                    print('请输入正确的操作')
            else:
                print('输入不能为空')
        else:
            print('您输入的商品不存在')
    else:
        print('输入不能为空')


# 删除商品
def delete():
    del_com_name = input('请输入您要删除的商品名称：').strip()
    if del_com_name:
        result = read_file()
        if del_com_name in result:
            del result[del_com_name]
            print('删除成功')
        else:
            print('您输入的商品不存在')
        write_file(result)
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
