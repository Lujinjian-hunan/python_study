# coding=utf-8
#非空即真，非0即真
# None {} （） [] ''
# username = input('username:')
# print(not username.split()) #取反
# # password = input('passeord')
# if username.split():
#     print('你输入的不为空', username)
# else:
#     print('username你输入是',username)



d = {'a':1,'b':2,'c':3,'d':0}

if d.get('d'):
    print('取到值了')
else:
    print('做另外的操作')