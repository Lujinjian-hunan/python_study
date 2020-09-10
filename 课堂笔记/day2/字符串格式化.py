# xxx,欢迎登陆
# xxx,今天要喝8杯水
import  datetime
name = '张三'
welcome = '张三,欢迎登陆'
today = datetime.datetime.today()

# 字符串格式化:
#   1、简单粗暴直接 +
# print(name + '，欢迎登陆' + '今天的日期是' + str(today))#不推荐
#   2、占位符,%d(数字) %s(字符串) %f（浮点类型）
# welcome = '%s，欢迎登陆，今天的日期是 %s' % (name,today)
# print(welcome)

# age = 18
# age_str = '你的年龄是 %d' % age
# score = 73.98312
# score_str = '你的成绩是 %.2f' %  score
# print(age_str)
# print(score_str)

#   3、大括号的方式
name2 = 'lily'
phone = '1381232523'
grade = 'tmz'
money = 5000
score = 98.133

addr = '北京'

welcome = '{name}，欢迎登陆，今天的日期是{today}'.format(today=today,name=name)
welcome2 = '{}，欢迎登陆，今天的日期是{}'.format(name,today)
print(welcome)
print(welcome2)

