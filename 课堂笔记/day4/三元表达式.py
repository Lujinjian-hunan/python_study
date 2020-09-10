# age = 18
#
# if age<18:
#     v = '未成年人'
# else:
#     v = '成年人'
# print(v)
#
# v1 = '未成年人' if age < 18 else '成年人'
# print(v1)
#
# a = [1,2,3,4,5,6]
# b = []
# for i in a:
#     b.append(str(i))
#
# c = [ str(i) for i in a]
# d = [ str(i) for i in a if i%2 == 0]
# print(c)
# print(d)

L1 = [1, 20, 13, 20, 30, 17]
L2 = ['成年人' if i > 18 else '未成年人' for i in L1]
print(L2)

L3 = [1,2,3,4,5,6]
L4 = [i if i %2 == 0 else -i for i in L3 if i %2 == 0]
print(L4)

print(-1 > 0)