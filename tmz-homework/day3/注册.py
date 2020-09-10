# 创建一个空字典，用于存放读取到的账号密码
users = {}
# 定义3个常量，存放大小写字母数字
CAP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOW = 'abcdefghijklmnopqrstuvwxyz'
NUM = '0123456789'
# 打开文件，读取文件里面存的数据
f = open('user.txt', 'a+', encoding='utf-8')
f.seek(0)
result = f.readlines()
# 先关闭文件，防止误操作
f.close()
# 把从文件中读取的数据传入usernames中，注意读取的数据带换行符
for user in result:
    # 去掉换行符然后用逗号把账号密码分割开
    new_user = user.strip().split(',')
    # 把读取的账号密码存入users字典里面
    username, password = new_user
    users[username] = password
# 循环输入3次，注册成功则提前退出
for i in range(3):
    username = input('请输入账号：').strip()
    password = input('请输入密码：').strip()
    cpwd = input('请确认密码：').strip()
    # 账号密码、确认密码的非空校验
    if len(username) == 0 or len(password) == 0 or len(cpwd) == 0:
        print('账号/密码不能为空')
    # 校验账号是否存在
    elif username in users:
        print('账号已存在')
    # 输入的密码长度的校验
    elif not 6 <= len(password) <= 12 or not 6 <= len(cpwd) <= 12:
        print(len(password))
        print(len(cpwd))
        print('密码长度要在6-12之间')
    # 校验两次输入的密码
    elif password != cpwd:
        print('两次输入的密码不一致')
    # 校验密码是否包含大小写数字,设置3个falge用于判断
    flage_A = False
    flage_a = False
    flage_n = False
    for x in password:
        if x in CAP:
            flage_A = True
            continue
        elif x in LOW:
            flage_a = True
            continue
        elif x in NUM:
            flage_n = True
            continue
    if flage_A is False or flage_a is False or flage_n is False:
        print('密码需包含大小写字母和数字')
    else:
        # # 打开文件，并把注册成功的账号密码写入文件中，注意要换行写入
        f = open('user.txt', 'a+', encoding='utf-8')
        f.writelines('\n' + username + ',' + password)
        # 关闭文件
        f.close()
        print('注册成功')
        break
# 循环完成还未注册成功提示错误次数超出限制
else:
    print('错误次数超出限制')
