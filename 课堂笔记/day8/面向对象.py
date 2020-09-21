class PersonManger: #经典类
    pass

class Person2():#新式类
    pass

class Person3(object):#新式类
    pass
import time

#析构函数
class Person:
    country = 'China'
    def __init__(self,name,sex):
        #构造函数，
        # print('self的内存地址,',id(self))
        self.name = name
        self.sex = sex
        self.__zl  = 200
        self.birthday = time.time()
        self.cry()

    @property
    def age(self):
        return int(time.time() - self.birthday)


    def __del__(self):
        print('我是%s 析构函数' % self.name)

    def run(self):
        print('%s 在run..' % self.name)


    def fly(self):
        print(' %s fly' % self.name)

    def cry(self):
        print('%s 哇哇哇哇' % self.name)



    #实例方法
    def say(self):
        print('my name is %s，sex is %s' %(self.name,self.sex))
        print('%s 斤'%self.__zl)
        print('我的国籍是 %s' % self.country)
        print('我的年龄是 %s' %self.age)

    @classmethod
    def putonghua(cls):
        print(cls.country)
        print('会说普通话')

    @staticmethod
    def suanuga():
        print('suanuga')


# Person.putonghua()
# Person.suanuga()
xh = Person('小黑','男') #实例化
xh.money = 100
xh.say()
print(xh.money)
# s='1'
# s=1.2
# s2=3
# l = []

# print('xh的内存地址',id(xh))
# xb = Person('小白','女')
# # print('xb的内存地址',id(xb))
#
# xb.fly()  #Person.fly(xh)
# xh.run() # Person.run(xb)
#
# del xb

# print('abc////////')


#db_back_
#db_back
#mysqlBackEveryDay

