#1、监控日志文件，找到每分钟请求大于200的ip地址，加入黑名单
import time
point = 0
while True:
    ips = {}
    f = open('access.log',encoding='utf-8')
    f.seek(point)
    for line in f:
        line = line.strip()
        if line:
            ip = line.split()[0]
            if ip in ips:
                ips[ip]+=1
            else:
                ips[ip] = 1
    point = f.tell()
    f.close()

    for ip in ips:
        count = ips[ip]
        if count>=200:
            print('要加入黑名单ip地址是：%s' % ip )
    time.sleep(60)
