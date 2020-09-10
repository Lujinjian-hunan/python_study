import xlwt

# book = xlwt.Workbook()
# sheet = book.add_sheet('students')
#
# sheet.write(0, 0, '编号')
# sheet.write(0, 1, '姓名')
# sheet.write(0, 2, '地址')
# sheet.write(0, 3, '年龄')
#
# stu = [
#     [1,'ds','bejing',51],
#     [2,'fd','shanghai',28],
#     [3,'zc','shanghai',16],
#     [4,'lhy','shanghai',21],
#     [5,'ylm','shanghai',35],
#     [6,'wxl','beijing',16]
#     ]
#
# for i in stu:
#     # print(i[0])
#     sheet.write(i[0], 0, i[0])
#     sheet.write(i[0], 1, i[1])
#     sheet.write(i[0], 2, i[2])
#     sheet.write(i[0], 3, i[3])
# book.save('students.xlsx')  # 如果后缀写成xlsx，使用微软的office打不开

# stus = [
#     [1, '张三', 'beijing', 19],
#     [2, '李四', 'shanghai', 28],
#     [3, '王五', 'shanghai', 16],
#     [4, '赵六', 'shanghai', 21]
#     ]
stus = [[1, 'niuhy', 'nv', 20, '111', '河北'], [2, 'Amy', '女', 18, '天马座', '天津'], [3, 'Bob', '男', 18, '天马座', '西北'], [6, 'lzh', '男', 38, '射手座', '北京'], [11, '尹路明', '女', 32, '31', 'shanghai'], [19, 'MLing', '女', 18, '处女座', '北京朝阳区'], [20, '魏强2', '男', 38, '射手座', '北京'], [33, '小白', '女', 18, '射手座', '北京'], [123241, 'lhy_test', None, None, 'tmz', None]]

table_herd = ['id', 'name', 'sex', 'age', 'class', 'addr']
stus.insert(0, table_herd)  # 插入表头
book = xlwt.Workbook()
sheet = book.add_sheet('sheet1')

# row = 0
# for stu in stus:  # 控制行
#     col = 0
#     for s in stu:
#         sheet.write(row, col, s)  # 控制列
#         col+=1
#     row+=1
# ages = [s[-1] for s in stus if type(s[-1]) != str]
# avg_age = round(sum(ages) / len(ages),2)
# print()
# content = '平均年龄:{}'.format(avg_age)
# sheet.write(row, 0, content)
# book.save('students.xlsx')


for row, stu in enumerate(stus):  # 控制行
    for col, s in enumerate(stu):  # 控制列
        sheet.write(row, col, s)

# ages = [s[-1] for s in stus if type(s[-1]) != str]
# avg_age = round(sum(ages) / len(ages),2)
# content = '平均年龄:{}'.format(avg_age)
# sheet.write(row+1, 0, content)

book.save('students.xlsx')

