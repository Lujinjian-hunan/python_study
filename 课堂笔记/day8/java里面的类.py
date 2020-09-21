class Lw:
    def driver(self):
        print('kaiche')

    def make_money(self):
        print('5000块钱')


class Xw(Lw):
    #重写
    def driver(self):
        print('开飞机')

    def make_money(self):
        super().make_money() #
        print('再挣5000块钱')

a = Xw()
a.make_money()


class Car: #基类
    def __init__(self,name):
        self.name = name
    def run(self):
        print('%s 在runxx' % self.name)

class Bmw(Car):
    def fly(self):
        print('xxx')

class Benz(Car):
    def swim(self):
        print('swim')

class Audi(Car):
    def liting(self):
        print('liting')



# def run(obj):
#     obj.run()
#
#
# c1 = Bmw('宝马')
# c2 = Benz('奔驰')
# c3 = Audi('奥迪')
#
# run(c1)
# run(c2)
# run(c3)

class E:
    def daka(self):
        pass

class E1:
    def daka(self):
        print('8:30')

class E2:
    def daka(self):
        print('9:30')

class E3:
    def daka(self):
        print('10:00')





