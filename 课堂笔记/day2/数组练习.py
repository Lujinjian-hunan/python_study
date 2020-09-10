# coding=utf-8
student_info2 = [
    [1,'刘海洋','北京'],
    [2,'hzy','北京'],
    [3,'ljj','北京']

]
# index = 0
# student_len = len(student_info2)#list的长度
# while index < student_len:
#     stu = student_info2[index]
#     #拆包
#     stuid,name,addr = stu
#     # stuid = stu[0]
#     # name = stu[1]
#     # addr stu[2]
#     sql = 'insert into studer values ({id},"{name}","{addr}");'.format(
#         id=stuid,name=name,addr=addr
#     )
#     print(sql)
#     index += 1

for stu in student_info2:
    stuid,name,addr = stu
    sql = 'insert into studer values ({id},"{name}","{addr}");'.format(
        id=stuid, name=name, addr=addr
    )
    print(stu)