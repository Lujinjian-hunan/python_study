# coding=utf-8
# username
# grade
# phone
# addr
# age
l = ['xiaohei','天马座','112342','北京','29']

d = {
        'username':'xiaohei',
        'id':'1',
        'grade':'天马座',
        'addr':'北京',
        'age':18
}
#添加一对键值
# d['money'] = 500
# d = d['age'] = 500
# d = d.setdefault('age','bmw')  # setdefault对已经存在的字段不会赋值
# print(d)

#通过key查找对应的values
# print(d['usernames'])  # 大括号查不到会报错
# print(d.get('age'))  # get查不到会返回None
# print(d)

#更新键值,修改存在的键对应的值
# d.update(addr='天津', age=20)
# print(d)

#删除，删除不存在的元素会报Key error
# d.pop('usernames')
# del d['usernames']
# print(d)

# print(d.keys()) # 获取字典里面的key
# print(d.values())   # 获取字典里面的values
# d.clear()   #清空字典

# users = {'fd':'123456',
#          'xzh':'45678'
# }
#
# username = 'fd'
# # print(d.keys())
# # print(username in users.keys())
# # print(username in users) #判断这个key是否存在
#
# print(d.items())    # 转成list
# # for k,v in d.items():   # 循环取值,可以取两个值，相当于拆
# #     print(k,v)
#
# for k in d: # 循环从字典中取值
#     print(k, d.get(k))  # 通过k查找对应的values
