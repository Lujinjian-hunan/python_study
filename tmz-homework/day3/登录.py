# 创建一个空字典，用于存放读取到的账号密码
users = {}
# 打开文件，读取文件里面存的数据
f = open('user.txt', 'a+', encoding='utf-8')
f.seek(0)
result = f.readlines()
# 关闭文件
f.close()
# 把从文件中读取的数据传入usernames中，注意读取的数据带换行符
for user in result:
    # 去掉换行符然后用逗号把账号密码分割开
    new_user = user.strip().split(',')
    # 把读取的账号密码存入users字典里面
    username,password = new_user
    users[username] = password
# 循环3次
for i in range(3):
    # 输入账号密码
    username = input('请输入账号：')
    password = input('请输入密码：')
    # 判断账号密码去空格后是否为空
    if len(username.strip()) == 0 or len(password.strip()) == 0:
        print('账号/密码不能为空')
    # 判断账号是否存在于字典的key中
    elif username not in users.keys():
        print('账号不存在')
    # 判断账号存在且字典中账号对应的密码是否等于输入的密码
    else:
        if users[username] == password:
            print('登录成功')
            break
        else:
            print('账号/密码错误！')
else:
    print('错误次数过多！')