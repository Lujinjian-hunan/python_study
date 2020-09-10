# coding=utf-8
import datetime
user = [
    ['fd','123456'],
    ['xzh','45678']
]
today = datetime.datetime.today()
error = 0 #错误次数
success = 0 #成功次数
passwordErr = 0

while True:
    if error == 3:
        print('次数超限')
        break
    if success == 1:
        print('欢迎{}登录，今天的日期是{}'.format(username,today))
        break
    username = input('请输入账号：')
    password = input('请输入密码：')
    if len(username) == 0:
        print("账号为空")
        error += 1
        continue
    if username.isspace():
        print('账号为空格')
        error += 1
        continue
    for i in user:
        print(i)
        if username in i:
           print(password.isspace())
           if len(password) == 0:
               print('密码为空')
               error += 1
               passwordErr = 1
               break
           if password.isspace():
               print('密码为空格')
               error += 1
               passwordErr = 1
               break
           if password not in i:
               print('密码不正确')
               error += 1
               passwordErr = 1
               break
           if password in i:
               print('密码正确')
               success += 1
               print(success)
               print('用户名：',username)
               break
    if success != 1 and passwordErr == 0:
        print('账号不正确')
        error += 1