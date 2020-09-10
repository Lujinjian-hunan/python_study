# coding=utf-8
users = {
    'fd','1234',
    'lhy','456'
}
for i in range(3):
    username = input('username:').strip()
    password = input('password:').strip()
    cpwd = input('apwd:').strip()
    if username =='' or password == '' or cpwd =='':
        print('账号/密码不能为空')
    elif password != cpwd:
        print('两次输入的密码不一致')
    elif username in users:
        print('账号已经存在')
    elif users[username] == password:
        print('注册成功')
        break
else:
    print('输入错误次数过多')
