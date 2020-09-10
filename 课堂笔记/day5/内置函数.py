# list dict tuple str int float set
# print input type id len
# sorted()
# zip()
# print(all([1, 2, 3, 4]))  # 判断可迭代的对象里面的值是否都为真
# print(any([0, 1, 2, 3, 4]))  # 判断可迭代的对象里面的值是否有一个为真
# print(bin(10))  # 十进制转二进制
# print(bool('s'))  # 把一个对象转换成布尔类型
# print(bytearray('abcde', encoding='utf-8'))  # 把字符串变成一个可修改的bytes
# print(callable('aa'))  # 判断传入的对象是否可调用
# print(chr(10))  # 打印数字对应的ascii
# print(ord('b'))  # 打印字符串对应的ascii码
# print(dict(a=1, b=2))  # 转换字典
# print(dir(1))  # 打印传入对象的可调用方法
# print(eval('[]'))  # 执行python代码，只能执行简单的，定义数据类型和运算
# print(exec('def a():pass'))  # 执行python代码
# print(filter(lambda x: x > 5, [12, 3, 12, 2, 1, 2, 35]))  # 把后面的迭代对象根据前面的方法筛选
# print(map(lambda x: x > 5, [1, 2, 3, 4, 5, 6]))
# print(frozenset({1, 2, 3, 3}))  # 定义一个不可修改的集合
# print(globals())  # 返回程序内所有的变量，返回的是一个字典
# print(locals())  # 返回局部变量
# print(hash('aaa'))  # 把一个字符串哈希成一个数字
# print(hex(111))  # 数字转成16进制
# print(max(111, 12))  # 取最大值
# print(oct(111))  # 把数字转换成8进制
# print(round(11.11, 2))  # 取几位小数
# print(sorted([2, 31, 34, 6, 1, 23, 4]))  # 排序
# dic = {1: 2, 3: 4, 5: 6, 7: 8}
# print(sorted(dic.items()))  # 按照字典的key排序
# print(sorted(dic.items(), key=lambda x: x[1]





# print(all([1,2,3,4]))  # 判断可迭代的对象里面的值是否都为真
# print(any([0, 1, 2, 3, 4]))  # 判断可迭代的对象里面的值是否有一个为真
# print(max(111, 12))  # 取最大值
# print(min(111, 12))  # 取最小值
# print(round(11.11982, 2))  # 取几位小数，会四舍五入
# print(dir(1))  # 打印传入对象的可调用方法
# print(bin(10))  # 十进制转二进制
# print(hex(111))  # 十进制转16进制
# print(oct(111))  # 十进制转8进制
# print(chr(98))  # 打印数字对应的ascii
# print(ord('b'))  # 打印字符串对应的/ascii码

# exec('def a():pass')  # 用来动态执行python代码
# s = '''
# for i in range(10):
#     print(i)
# '''
# exec(s)

# print(eval('[]'))  # 执行python代码，只能执行简单的，定义数据类型和运算
# result = eval('1+1')
# print(result)

# print(filter(lambda x: x > 5, [12, 3, 12, 2, 1, 2, 35]))  # 把后面的迭代对象根据前面的方法筛选
# filter  # 过滤
# def oushu(number):
#     if number%2 == 0:
#         return True
#
# l = range(1,10)
# l2 = []
# for i in l:
#     if oushu(i):
#         l2.append(i)

# filter(oushu)
# result = list(filter(oushu, l))
# result2 = list(map(oushu,l))
# print(l2)
# print(result)
# print(result2)

#filter会自动循环你传给他的list，然后把list里面的
#每一个元素传给指定的函数，如果这个函数结果返回的是
#true，那么就保留这个元素

# print(map(lambda x: x > 5, [1, 2, 3, 4, 5, 6]))

# map(oushu, l)  # 每一个元素传给指定的函数，吧这个函数的结果报存下来
# result1 = list(map(oushu, l))
# print(result1)


# def test():
#     a = 1
#     b = 2
#     print(locals())  # 获取当前函数里面的局部变量
#     print(globals())  # 获取当前文件里面的全局变量
#
#
# test()
# print(globals())
# zip()
# a = ['zs','li','ww']
# b = ['123','456','789']
# c = ['1','2','3']
# [
#     ['zs','123','1'],
#     ['zl','lq','tj'],
#     ['123','456','789']
# ]

# for username,password,c in zip(a, b, c):
#     print(c, username, password)

# for x in zip(a, b , c):
#     print(x)


# print(ascii('哈哈'))
# print(ascii('hello world'))

# print('{},{}'.format('hello', ' world'))  # 这种方式参数要按顺序排列
# print('{b},{a}'.format(a = 'hello', b = 'python')) # 用这种方式参数可以不按顺序排列
# print('{:.0f}'.format(5.244))  # 也可以处理数字，比如去掉小数
# s = (1,2,3,4,5,6)

# print(abs(-10))
# print(abs(-1.25))
# n1 = all([1,2,3,True])
# n2 = all([{},[],None,False])
# print (n1)
# False
# n2 = any([1,0,"",[]])
# print (n2)
# True
# ascii()
# print(bin(10))
# print(bin('10'))
# print(bin(10.52))
# print(bool(10))
# print(bool(0))
# print(bool('10'))
# print(bool(''))
# print(bytearray())
# print(bytearray([1,2,3]))
# print(bytearray('hello', 'utf-8'))

# print(bytes([1,2,3,4]))
# print(bytes('hello','ascii'))
# print(callable(0))
# print(callable('hello'))
#
# def add(a,b):
#     return a+b
#
#
# add(1,2)
# print(callable(add))
# print(chr(65))  # 十进制
# print(chr(0x41))  # 十六进制


# c = compile('hello','','exec')
# print(c)

# print(complex(1, 2))
# print(complex(1))  # 数字
# print(complex("1"))  # 当做字符串处理

# class Coordinate:
#     x = 10
#     y = -5
#
#
# point1 = Coordinate()
# print('x = ', point1.x)
# print('y = ', point1.y)
#
# delattr(Coordinate, 'y')
#
# print('--删除 y 属性后--')
# print('x = ', point1.x)
#
# # 触发错误
# print('y = ', point1.y)

# print(dict())                        # 创建空字典
# print(dict(a='a', b='b', t='t'))     # 传入关键字
# print(dict(zip(['one', 'two', 'three'], [1, 2, 3])))   # 映射函数方式来构造字典
# print(dict([('one', 1), ('two', 2), ('three', 3)]))    # 可迭代对象方式来构造字典
# print(dir('1'))
# print(eval('1+1'))
# def oushu(n):
#     return n % 2 == 0
#
#
# L = filter(oushu, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# newlist = list(L)
# print(newlist)


# print(frozenset([1, 2, 3, 3]))
# print(type(frozenset([1, 2, 3, 3])))

print(hash('test'))  # 字符串
print(hash(1))  # 数字
print(hash(str([1,2,3])))  # 集合
print(hash(str(sorted({'1':1}))))  # 字典
