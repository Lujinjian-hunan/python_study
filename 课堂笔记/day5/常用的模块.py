import os, random, sys, time, string


# random  生成随机数
# print(random.random())  # 生成0-1之间的随机数
# print(random.randint(1,10))  #生成1-10之间的随机整数
# print(random.uniform(1,10))  #生成1-10之间的随机小数
# print(random.choice(string.ascii_lowercase))  # 随机生成一个元素
# print(random.sample(string.ascii_lowercase,3))  # 随机选择多个元素并生成一个列表，数量不能超过原对象的元素上限

# print(random.sample('0123456789', 3))
# print(random.sample('0123456789', 15))

# l = [random.choice(string.digits) for i in range(6)] # 取的这几个元素里面，会有重复的
# l2 = random.sample(string.digits,6)  # 取的这几个元素里面，它不会有重复的
# #
# print(l)
# print(l2)
#
# print(''.join(l))
# print(''.join(l2))


# print(random.shuffle)  # 洗牌，打乱顺序
l = [1,2,3,4,5,6,7,8]
print('打乱之前：', l)
random.shuffle(l)
print('打乱之后：', l)
#
#
# # sorted()  # 排序
# s = '3265432145132asdasda'
# result = sorted(s, reverse=True)  # 反转
# print(result)

# d = {
#     'fd':100,
#     'ds':93,
#     'lhy':88,
#     'hzy':35
# }

# for i in d[]:
# result = sorted(d, reverse=True)  # 反转
# print(result)

# c = d.values()
# print(c)
# result = sorted(c,reverse=True)
# print(result)
# c = d.items()
# print(c)
# result = sorted(c, key=lambda  x:x[1],reverse=True)  # 按照字典的值来排序
# result1 = sorted(c,reverse=True)  # 默认按照key来排序
# print(result)
# print(result1)
