# coding=utf-8
students = ['lhy','hzy','fd']
#录入学生信息，判断学生是否存在，如果已经存在，提示它。然后继续添加，
#直到它输入over，结束
while 1 > 0:
    stu = input('请输入学生信息：')
    if stu == 'over':
        print('所有学生信息是',students)
        break
    elif students.count(stu)>0:
        print('学生信息已经存在')
    else:
        students.append(stu)
        print('已经添加'.format(stu))