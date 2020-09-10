def hhh(name,age,sex):
    print(name)
    print(age)
    print(sex)

l = ['xh',18,'nan']
d = {'name':'xh','age':18,'sex':'nan'}
hhh(*l)# 'xh',18,'nan'
hhh(**d)#name=xh,age=18,sex=nan