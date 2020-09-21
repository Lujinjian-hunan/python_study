import logging
from loguru import logger
import time
#debug #调试信息，最低的级别
#info #正常的提示信息
#waring #警告信息
#error #出错了 # 50 - 100


#exception #程序出异常了 sql执行出错
import sys


logger.remove()  # 清除它的默认设置设置
fmt = '[{time}][{level}][{file.path}:line:{line}:function_name:{function}] ||msg={message}'
# level file function module time message
# logger.add(sys.stdout, level='INFO', format=fmt)  # 咱们本地运行的时候，在控制台打印
# logger.add('wxl.log',level='DEBUG',format=fmt,encoding='utf-8',enqueue=True,rotation='1 s',retention='10 seconds')#写在日志文件里面
logger.add('wxl.log', level='DEBUG', format=fmt, encoding='utf-8', enqueue=True, rotation='1 day')  # 写在日志文件里面

def fd():

    logger.remove()#清除它的默认设置设置
    fmt = '[{time}][{level}][{file.path}:line:{line}:function_name:{function}] ||msg={message}'
    #level file function module time message
    logger.add(sys.stdout,level='INFO',format=fmt)#咱们本地运行的时候，在控制台打印
    # logger.add('wxl.log',level='DEBUG',format=fmt,encoding='utf-8',enqueue=True,rotation='1 s',retention='10 seconds')#写在日志文件里面
    logger.add('wxl.log',level='DEBUG',format=fmt,encoding='utf-8',enqueue=True,rotation='1 day',retention='10 days')#写在日志文件里面

    # rotation可以设置大小，超过多大就产生一个新文件 1 kb ,500 m ,1 g
    # rotation可以多长时间，1 day   1 hour
    # rotation几点创建新文件，00:00  1:00

    # retention = 7 days #多长时间后会删除以前产生的日志,当前的日志不会受影响
    #enqueue=True，异步写日志 #同步
    #队列
    #消息队列
    for i in range(20):
        time.sleep(1)
        logger.debug('程序开始运行了')
        logger.debug('开始连接mysql')
        logger.info('mysql配置xxxx')
        logger.warning('警告，磁盘空间即将不足')
        logger.error('程序出错了')

fd()

