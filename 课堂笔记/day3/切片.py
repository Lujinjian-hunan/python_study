# coding=utf-8
# 切片是list范围取值的一种方式

# import string
# print(string.ascill_lowercase)
# print(string.ascill_uppercase)
# print(string.digits)
# print(string.ascill_letters)
# print(string.punctuation)

# l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']   #切片的时候是顾头不顾尾的
# print(l[0:3])
# print(l[2:-1])
# print(l[0:10:2]) #最后一位表示步长
# print(l[-1:-8:-2])  #步长如果是负数的话，那么取值的时候就从右往左开始取，同时你的开始和结束下标也要写成负数


#循环删除list里面的元素会导致下标变化，导致最终结果错误
# l = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# for i in l:
#     if i% 2 ==0:
#         l.remove(i)
# print(l)
#解决办法一，再弄一个list，循环新的list，删除之前的list里面的元素
# l = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# print(id(l))
# print(id(l2))
# for i in l2:
#     if i% 2 ==0:
#         l.remove(i)
# print(l)


#浅拷贝/深拷贝 如果复制了一个变量，这两个变量其中一个变了之后，不应该影响另外一个的情况下，就要用深拷贝
# 浅拷贝
# l = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = l
# print(id(l))
# print(id(l2))
# for i in l2:
#     if i% 2 ==0:
#         l.remove(i)
# print(l)
# 深拷贝
# import copy
# l = [0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9]
# l2 = copy.deepcopy(l)
# print(id(l))
# print(id(l2))
# for i in l2:
#     if i% 2 ==0:
#         l.remove(i)
# print(l)