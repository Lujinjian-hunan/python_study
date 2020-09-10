# students = '张三，李四，王五'

# 数组、列表、list
# students_new = ['张三','李四','王五']
#                 0      1      2
#编号，索引、下标、角标
# print(students_new[1])
# print(students_new)
# #增加元素
# students_new.append('赵六')
# #修改
# students_new[2] = '赵四'
# #删除
# students_new.pop(1)#传入指定的下标，删除元素
# students_new.remove('赵四')#删除指定的元素
#
# print(students_new)
# # print(students_new[3])
# print(students_new[-1])
# print(students_new[0])

#方法
# students_new.count()
# students_new.index()
# students_new.extend()
# students_new.reverse()
# students_new.sort()

#students_new.clear()#清空list
# print('清空后的',students_new)
#
# zs_count = students_new.count('张三')#统计这个list元素里面元素出现的次数
# print('count',zs_count)
#
# print('index',students_new.index('张三'))#找到某个元素的下标
#
# user = ['刘七','周八']
# students_new.extend(user)#把一个列表里面的元素加入到另一个列表里面
# print(students_new)
#
# students_new.reverse()#翻转list 0,1,2,3,4,5,6 6,5,4,3,2,1,0
# print('reverse之后的',students_new)
#
# number = [2,565,54,758,112,14,365]
# number.sort()#排序,默认是升序
# print('sort升序',number)
# number.sort(reverse=True)#降序
# print('sort降序',number)

#多维数组
students_info = [
    [1,'张三','北京'],
    [2,'李四','上海'],
    [3,'王五','天津']
]#二维数组

students_info2 = [
    [1,'张三','北京',['bmw','benz','audi']],
    [2,'李四','上海',['bmw', 'benz', 'audi']],
    [3,'王五','天津']
]#三维数组

students_info[0][-1] = '山东'
students_info2[0][-1].append('tesla')
print(students_info)
print(students_info2)