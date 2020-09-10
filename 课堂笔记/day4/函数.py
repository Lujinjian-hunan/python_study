#函数、方法
import string
import datetime
def hello(s):
    if s == 1:
        print('hello world')
    else:
        print('aaa')
    return


hello(2)
# def hello(a, b): #定义函数,提高代码的复用性
#     c = a+b
#     print(c)
#     return

# print(e)
# def baoshi():
#     print('当前时间',datetime.datetime.today())
#
# def check_password(password):#校验密码是否合格,必传参数，位置参数
#     password_set = set(password)
#     if password_set & set(string.digits) and password_set & set(string.ascii_lowercase) \
#             and password_set & set(string.ascii_uppercase):
#         print('合法')
#         return True
#     else:
#         print('不合法')
#         return False
#
# # with open('f','w',encoding='utf-8') as fw:
# #     fw.write(xxx)
#
# def write_file(file_name,content):
#     with open(file_name,'w',encoding='utf-8') as fw:
#         fw.write(content)
#
# def read_file(file_name):
#     with open(file_name,encoding='utf-8') as fr:
#         result = fr.read()
#         return result
# # write_file(content='1234',file_name='a.txt')
# # write_file('a.txt',content='absdfs')
# # write_file('a.txt','12235236')
#
#
# #默认值参数
#
# def op_file(file_name,content=None):
#     print(content)
#     if content:
#         write_file(file_name,content)
#     else:
#         result = read_file(file_name)
#         return result
#
# print( op_file('1.txt') )
# op_file('1.txt','sdfdssgsdgsdg')