import os
import time
# 循环读取logs文件夹下的文件
for cur_path, dirs, files in os.walk(r'.\logs'):
    print('正在%s目录下查找' % cur_path)
    for file in files:
        if file.endswith('log'):
            # 分割文件名，获取文件名中的时间
            file_name = file.split('.')[0]
            file_time = file_name.split('_')[-1]
            # 把获取到的时间转为时间戳
            time_tulpe = time.strptime(file_time, '%Y-%m-%d')
            time_stamp_old = time.mktime(time_tulpe)
            # 计算3天前的时间戳
            three_day = time.time() - 3 * 24 * 60 * 60
            # 拼接文件路径
            file_path = os.path.join(cur_path, file)
            # 判断文件的时间戳是否小于3天前的时间戳，是的话就删除
            if time_stamp_old < three_day or os.path.getsize(file_path) == 0:
                os.remove(file_path)
                print('删除日志成功')