import time

import redis

r = redis.Redis(host='118.24.3.40',
                password='HK139bc&*',
                port=6379,
                db=14,
                decode_responses=True
                )

#string
#hash


#string
# r.set('矿泉水','{"price":111,"count":11}')
# #bytes #字节类型
# data = r.get('矿泉水').decode()
# r.delete('矿泉水')
# r.set('矿泉水','xxxx')
#
# expire_time = 60 * 60 * 24
# r.set('fd_session','sdgx312vsdrq',expire_time)

#{"kqs":{xxx},"笔":{xxx}}

# r.hset('students','fd','{"money":19999}')
# r.hset('students','ds','{"money":19111999}')
# r.hset('students','lhy','{"money":19111999}')
# r.hset('students','ljj','{"money":19111999}')

# print(r.hget('students','ds'))
# d = r.hgetall('students')
# print(d)
# r.hdel('students','ds')
#r.delete('students')
# r.expire('students',100)#指定某个key的过期时间

# new_d  = {}
# for k,v in d.items():
#     new_d[k.decode()] = v.decode()
# print(new_d)

# s = '你好啊'
# print(s.encode())#变成bytes类型的就行了
#0-16

#加密
#a -> mysql
# key是什么 key的类型什么
# print(r.keys())
# print(r.keys('s*'))
# print(r.type('stu'))
# print(r.type('students'))
# print(r.flushdb()) #清空当前数据库里面所有的key
# print(r.flushall())#清空所有数据库里面所有的key


#管道，批量操作
# p = r.pipeline()#建立管道
# p.exists('students123')
# p.hgetall('students')
# # p.hset('students','fd','{"money":19999}')
# # p.hset('students','ds','{"money":19111999}')
# # p.hset('students','lhy','{"money":19111999}')
# # p.hset('students','ljj','{"money":19111999}')
# s = p.execute() #执行,返回一个list，这个list里面是每个命令执行的结果
# print(s)
# print(r.exists('students123'))

# start_time = time.time()
# for i in range(100):
#     r.set('key%s'%i,'%s'%i)
# print('不用管道的时间',time.time() - start_time)
#
#
# start_time = time.time()
# p = r.pipeline()
# for i in range(100):
#     p.set('pipline_key%s'%i,'%s'%i)
# p.execute()
# print('用管道的时间',time.time() - start_time)

r.set('product:kqs','{"count":1,"price":5555}')
r.set('product:apple','{"count":1,"price":5555}')
r.set('product:banana','{"count":1,"price":5555}')

#a服务器 -》迁移
#b服务器，redis


r = redis.Redis(host='118.24.3.40',
                password='HK139bc&*',
                port=6379,
                db=14,
                decode_responses=True
                )
r2 = redis.Redis(host='118.24.3.40',
                password='HK139bc&*',
                port=6378,
                db=14,
                decode_responses=True
                )

p = r2.pipeline()

for k in r.keys():
    key_type = r.type(k)
    if key_type == 'string':
        value = r.get(k)
        p.set(k,value)
    elif key_type=='hash':
        hash_data = r.hgetall(k) #{'xx':xxx}
        for filed,data in hash_data.items():
            p.hset(k,filed,data)

p.execute()