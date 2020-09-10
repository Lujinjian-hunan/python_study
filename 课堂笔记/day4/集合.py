#set
#天生去重,无序的
l = [1,2,11,1,1,3,5,7]
l2 = {1,2,3,4,5,1,1}
l3 = set()
s = set(l)
print(s)
print(l2)

#交集 并集 差集
l3.add(1)#新增元素
l3.remove(1)#删除元素
l3.update(l2) #把一个集合加入到另外一个集合里面

stu1 = ['fd','wxl','zjr','lhy']#自动化
stu2 = ['fd','wxl','dsx','cc']#性能

stu1_set = set(stu1)
stu2_set = set(stu2)

print(stu1_set.intersection(stu2_set))#取交集
print(stu1_set & stu2_set) #取交集
import string

password = 'abc123A'

password_set = set(password)

if password_set & set(string.digits) and password_set & set(string.ascii_lowercase) \
    and password_set & set(string.ascii_uppercase):
    print('密码合法')
else:
    print('不合法')

#并集，把两个集合合并到一起
s1 = {1,2,3,4}
s2 = {4,5,6,7}

print(s1.union(s2))
print(s1 | s2)

#差集
print(s1.difference(s2)) #在一个集合里面存在，在另外一个集合中不存在的
print(s1 - s2)

#对称差集
print(s1 ^ s2)
print(s1.symmetric_difference(s2))

for s in s1:
    print(s)