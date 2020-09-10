# coding=utf-8
# s = '  abcsdg  sgssdgsgsgd  '
#统计字符串出现的次数
# s.count()
# print(s.count('a'))

#找字符串的下标，找不到会报错
# s.index()
# print(s.index('s'))
# print(s.index('a', 0,10))
# print(s.find('a', 0,10))    #找字符串的下标，找不到返回not found

#去首尾空格和换行符
# s.strip()
# print(s.strip())
# print(s.strip('a'))    #也可以用去去掉指定字符

#去右边空格
# print(s.rstrip())

#去左边空格
# print(s.lstrip())

#替换指定字符，默认全部替换
# s.replace()
# print(s.replace('s','S'))
# print(s.replace('s','S',1))    #可以指定替换次数
# words_list = ['傻逼','傻b','煞笔','煞比','sb']
# content = input('请输入：')
# for word in words_list:
#     content = content.replace(word,'*')
# print(content)

#格式化字符串
# s.format()
# print('{name},{value}'.format(name=1, value =2))
#字典形式
# print('{name},{value}'.format_map({"name":"fd", "value":1000}))
# s = '1'
# if len(s)<3:
#     if len(s)==1:
#         s='00'+s
#     elif len(s)==2:
#         s='0'+s
#     else:
#         s='0'

#补0，输入多少就补多少
# print(s.zfill(4))

# s = '1234shi.py'
#是否为纯数字
# s.isupper()
# print(s.isupper())

#判断是否以某某结尾
# s.endswith()
# print(s.endswith('.py'))

#判断是否以某某开头
# s.startswith()
# print(s.startswith('123'))

#补充字符串长度
# s.center()
# print('欢迎登录'.center(50,'*'))

#空格隔开的英文首字母变成大写
# print('ma car'.title())

#判断字符串是否全是大写
# print(''.isupper())# print(s.isupper())

# 判断字符串是否全是小写
# s.islower()
# print(s.islower())

#把首字母变成大写
# s.capitalize()
# print('ma car'.capitalize())
# s='傻逼 傻b 煞笔 煞比 sb,傻B shabi'

#分割字符串，默认以空格和换行符分割
#s.split()
# print(s.split())
# print(s.split(','))
# print(s.split('5'))    #输入不存在的字符，会把字符串直接存为list

#连接list里面的每个元素的
# s.join()
l = ['傻逼', '傻b', '煞笔', '煞比', 'sb', '傻B', 'shabi']
l_str = ''.join(l)
print(l_str)
print(type(l_str))





# s.upper()
# s.lower()
# s.isdigit()
# s.endswith()
# s.startswith()
#
# s.format_map()
# s.center()
# s.title()
# s.isspace()

# s.lower()
# s.join()