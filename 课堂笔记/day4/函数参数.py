# #必传参数（位置参数）、默认值参数
# #可选参数（参数组）、关键字参数
# import json
# def send(*args):
#     for p in args:
#         print('发短信给xxx%s'%p)
#
# # send()
# # send(110)
# # send(110,120,119)
#
#
#
# #可选参数，它不是必传的，不限制参数个数，它是把参数放到了一个list里面
#
#关键字参数，它不是必传的，不限制参数个数,它是把参数放到了一个字典里面，
# 但是它传参的时候必须得用关键字的方式
# def send_sms(**kwargs):
#     print(kwargs)
#
# send_sms()
# send_sms(xzh='晚上好')
# send_sms(lhh='新年好',fd='生日快乐',lyh='新婚幸福')
#
#
# def nb_func(name,age,country='China',sex='女',*args,**kwargs):
# #     #1、必填参数
# #     #2、默认值参数
# #     #3、参数组
# #     #4、关键字参数
#     print(name)
#     print(age)
#     print(sex)
#     print(country)
#     print(args)
#     print(kwargs)
#
# nb_func('xh',18,'abc','efg','hhh',name1=1,b=2,c=3)
#
# nb_func('xh',18,'japan','nan','abc','efg','hhh','2335','23532',a=1,b=2,c=3)

# def user_info(name,*args ):
#     print(name)
    # print(age)
    # print(country)
    # print(sex)
#     print(args)
#     return
#
#
# user_info('张三','holle','world','pythom')
# user_info(name='张三')



def user_info(name, age = 18):
    print(name)
    print(age)
    return


user_info('张三',20)
user_info('张三')  # 不传默认值参数，则默认返回age为18