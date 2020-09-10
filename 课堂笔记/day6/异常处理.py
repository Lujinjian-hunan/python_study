import traceback
# a = [1,2,3]
# a[4]
# float('s.3')
# 捕捉异常
# noinspection PyBroadException
try:
    # '1'+'2'
    2/0

# except TypeError as e:
#     print(e)
#     print('出错了')
#
# except ZeroDivisionError:
#     print('除数不能为0')
except BaseException as e:
    # 调用堆栈信息
    # traceback.print_exc() # 打印异常信息
    print('错误信息：', e)
    print('错误信息：', traceback.format_exc())
else:
    print('没有异常')
finally:
    print('aaa')
