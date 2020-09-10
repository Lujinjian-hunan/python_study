import os

# print(os.listdir(r'C:\Users'))  # 获取某个目录下的内容
# print(os.name)  # 打印操作系统

# 创建文件夹
# os.mkdir(r'D:\python')  # 文件已经存在会报错，父目录不存在的时候会报错

# os.makedirs(r'D:\java\java')  # 父目录不存在的时候，会创建父目录
# print(os.listdir(r'D:\java'))

# 删除文件
# print(os.listdir(r'D:\python'))
# os.remove(r'D:\python\test.txt')  # 只能删除文件，不能删除文件夹
# print(os.listdir(r'D:\python'))


# 删除文件夹
# os.rmdir()  # 只能删除空的文件夹，不为空会报错

# 重命名
# print(os.listdir(r'D:'))
# os.rename(r'D:\java',r'D:\python')  # 文件和文件夹都可以
# print(os.listdir(r'D:'))


# 获取当前所在的目录
# print(os.getcwd())

# os.chdir()  # 进入某个目录里面
# os.chdir(r'D:\Program Files')
# print(os.getcwd())

# 获取系统环境变量里面配置的内容
print(os.environ)

# 执行操作系统命令
# print(os.system('ipconfig'))  # 他只能帮你执行，不能拿到返回结果，返回的是命令执行是否成功，如果命令是0，代表执行成功

# os.popen()  # 执行命令，可以拿到结果
# result = os.popen('ipconfig').read()
# print(result)

# 获取当前系统路径分隔符
# print(os.path.sep)

# print(os.path.isfile('a.py'))  # 判断是否是文件
# print(os.path.isdir('a.py'))   # 是否是文件夹
# print(os.path.exists('a.py'))  # 文件/文件夹是否存在
# print(os.path.getsize('a.py'))   # 获取文件大小
# print(os.path.getctime('a.py'))  # 创建时间
# print(os.path.getmtime('a.py'))  # 修改时间
# print(os.path.getatime('a.py'))    # 最后一个访问时间

# 分隔路径和文件名
# os.path.split()
# print(os.path.split(r'D:\Users\Administrator\PycharmProjects\tmzlearn\day5\a.py'))

# 连接路径和文件名
# os.path.join()
# p = 'e:'+os.path.sep+'movies'+os.path.sep+'欧美大片'
# print(p)
# print(os.path.join('e:','\movies','欧美大片','复仇者联盟.mp4'))

# 把相对路径转换为绝对路径
# print(os.path.abspath(r'..\day4\a.json'))
# print(os.path.abspath(__file__))  # __file__代表当前文件
# ..\day4\a.json 相对路径 两个点代表上级目录
# D:\Users\Administrator\PycharmProjects\tmzlearn\day4\a.json  绝对路径

# 取父目录
# os.path.dirname()
# base_path = os.path.dirname(__file__)
# print(base_path)
# print(os.path.join(base_path, 'a.py'))

# 循环读取文件夹内的所有内容
# os.walk()
# for cur_path, dirs, files in os.walk(r'D:\Users\Administrator\PycharmProjects\tmzlearn'):
#     print('正在%s目录下查找'%cur_path)
#     for file in files:
#         if file.endswith('.py') or file.endswith('.avi'):
#             print('发现小电影在%s目录下'%cur_path)
#             break

    # print(cur_path,dirs,files)