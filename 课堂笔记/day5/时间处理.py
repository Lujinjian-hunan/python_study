import time

# 时间戳 一串数字 从unix元年开始
# 格式化好的时间  2020-08-29 17:24:38
# 20200829172438

# print(20200829 + 28)

# print(time.time())  # 获取当前时间戳
# print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 格式化时间

# seven = int(time.time()) + 60*60*24*7
# print(seven)
#
str_time = '2020-08-29 17:31:02'
# str_time = time.localtime()
time_stamp = 1599298546

# 时间元组

# 时间戳转格式化好的时间
lt = time.localtime(time_stamp) # 获取当前时间
bt = time.gmtime(time_stamp)  # 标准时区时间
print(lt)
print(bt)
print(time.strftime('%Y-%m-%d %H:%M:%S',lt))

# 格式化好的时间转时间戳
time_tulpe = time.strptime(str_time, '%Y-%m-%d %H:%M:%S')
time_stamp_nwo = time.mktime(time_tulpe)
print(time_stamp_nwo)