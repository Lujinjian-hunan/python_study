# f = open('user.txt','a+',encoding='utf-8')
# f.seek(0)
# usernames = []
# for line in f.readlines():
#     line = line.strip()
#     if line:
#         username = line.split(',')[0]
#         usernames.append(username)
# for i in range(3):
#     username = input('username:').strip()
#     password = input('password:').strip()
#     cpassword = input('cpassword:').strip()
#     if not username or not password or not cpassword:
#         print('账号/密码不能为空')
#     elif len(password)<6 or len(password) > 12:
#         print('密码长度在6-12之间')
#     elif password != cpassword:
#         print('两次输入的密码不一致')
#     else:
#         l = u = d = False
#         for p in password:
#             if p.islower():
#                 l = True
#             elif p.isupper():
#                 u = True
#             elif p.isdigit():
#                 d = True
#         if not l or not u or not d:
#             print('密码必须包含大小写字母、数字')
#         elif username in usernames:
#             print('用户已经存在了')
#         else:
#             f.write('%s,%s\n'%(username,password))
#             print('注册成功')
#             break
# else:
#     print('错误次数过多！')
#
# f.close()

#登录

f = open('user.txt',encoding='utf-8')
users = {}
for line in f.readlines():
    line = line.strip()
    if line:
        username = line.split(',')[0]
        password = line.split(',')[1]
        users[username] = password #{'fd':12345,'liuhaiyang':123456}
f.close()

for i in range(3):
    username = input('username:').strip()
    password = input('password:').strip()
    if not username or not password:
        print('账号/密码不能为空')
    elif len(password)<6 or len(password) > 12:
        print('密码长度在6-12之间')
    elif username not in users:
        print('用户不存在！')
    elif password != users.get(username):
        print('密码错误！')
    else:
        print('欢迎登录')
        break
else:
    print('错误次数超限')

