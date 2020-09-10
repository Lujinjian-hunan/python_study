# coding=utf-8
# 引入时间库
import datetime

# 定义变量并赋值
user = [
    ['fd', '123456'],
    ['xzh', '45678']
]
today = datetime.datetime.today()   # 获取时间，命名为today
error = 0   # 错误次数
success = 0  # 成功次数
First_name = ''  # 用于输出欢迎XXX登录时调用

# 添加一个无限循环，为了循环输入账号密码
while True:
    # 判断错误次数，超出3次输出结果，结束while循环
    if error == 3:
        print('错误次数超出限制')
        break
    # 判断成功次数，如果成功，则输出结果，结束while循环
    if success == 1:
        # 输出结果，{}为变量,format格式化字符串
        print('欢迎{}登录，今天的日期是{}'.format(First_name, today))
        break
    # 用户输入账号密码
    username = input('请输入账号：')
    password = input('请输入密码：')
    # 判断账号为空的话提示账号为空，结束本次循环继续输入账号密码
    if username == '':
        print("账号不能为空")
        error += 1
        continue
    # 判断账号为空格的话提示账号为空格，结束本次循环继续输入账号密码
    elif username.isspace():
        print('账号为空格')
        error += 1
        continue
    # 如果账号不为空，用for循环取user里面的值，输出为i
    else:
        for i in user:
            # 拆包
            userName, passWord = i
            # 为First_name赋值
            First_name = userName
            # 判断输入账号是否等于i里面的账号，如果等于继续往下走，不等于则继续循环查询下一个结果
            if username == userName:
                # 判断密码为空的话提示密码为空，结束for循环，并且错误次数+1
                if password == '':
                    print('密码不能为空')
                    error += 1
                    break
                # 判断密码为空格的话提示密码为空格，结束for循环，并且错误次数+1
                elif password.isspace():
                    print('密码为空格')
                    error += 1
                    break
                # 判断密码是否正确，正确的话结束for循环，并且成功次数+1
                elif password == passWord:
                    print('密码正确')
                    success += 1
                    break
                # 以上条件不成立时输出密码不正确
                else:
                    print('密码不正确')
                    error += 1
                    break
        # 如果for循环结束完成后还没查询到账号，则提示账号不正确，并且错误次数+1
        else:
            print('账号不正确')
            error += 1
