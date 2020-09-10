# def test():
#     print('hello')
#
# def test2():
#     return 1,2,3
#
#
# #如果一个函数没有写返回值的话，返回的就是None
# #如果函数有多个返回值，那么返回的是一个元组
#
# a,b,c = test2()
#
# #全局变量:一般定义在代码的最上面，大家都可以用的
# #局部变量：在函数里面定义的变量，都是局部变量

file_name = 'a.txt'
country = 'China'
#list、dict、set不需要用global来声明了
#str、int、float、tuple、bool#需要的
def say():
    print(file_name)
    word = 'Nihao'
    print(country)
    print(word)

def zhucheng():
    country = 'Japan'
    print(country)

def update_file_name():
    global file_name
    file_name = 'a.json'

print(file_name)
update_file_name()
print(file_name)




# money = 500
#
# def test(consume):
#     return money - consume
#
#
# def test1(money):
#     return test(money) + money
#
#
# money = test1(money)
#
# print(money)


# def test():
#     global a
#     a = 5
#
#
# def test1():
#     c = a + 5
#     return c
#
# test()
# res = test1()
# print(res)

# def my_fb(s):
#     a = 0
#     b = 1
#     if s <= 1:
#         print('error')
#     for i in range(s):
#         a, b = b,a+b
#         print(a)
#
#
# my_fb(int(1))


# def my_fb(s):
#     a = 0
#     b = 1
#     for i in range(s):
#         a, b = b,a+b
#         if a >= s:
#             break
#         print(a)
#
#
#
# my_fb(100)


# def fibonacci(num):
#     fibs = [0,1]
#     for i in range(num-2):
#         fibs.append(fibs[-2]+fibs[-1])   #倒数第二个+倒数第一个数的结果，追加到列表
#     return(fibs)
# c = fibonacci(5)
# print(c)



# def my_fb1(s):
#     a = 0
#     b = 1
#     # if s <= 1:
#     #     print('error')
#     for i in range(s):
#         a, b = b,a+b
#     return a
#
#
# def my_fb2(result):
#     a = 0
#     b = 1
#     # if result <= 1:
#     #     print('error')
#     while True:
#         a, b = b,a+b
#         if a >= result:
#             break
#         print(a)
#
#
# my_fb2(my_fb1(10))