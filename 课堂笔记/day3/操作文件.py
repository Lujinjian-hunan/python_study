# coding=utf-8
# open('a.txt')   #当前路径打开这个文件
# open(r'D:\a.txt')   #打开D盘下的a.test文件，用绝对路径时前面加个r，意思取原字符

# f = open('l.txt', 'r',encoding='utf-8')  #三种模式 w r a
# result = f.read()  #读取到的内容是字符串
# result = f.readlines()  #读取到的内容放入list里
# result = f.readline()   #读一行
# print(result)
# namers = ['fd','lhy','hzy']
# nambers = [1,2,3,4,5,6]
# result =f.write('acv')  #这个会覆盖源文件内容,并且文件不存在会新建一个文件且写入数据，不能写入list
# result =f.writelines('acv')  #传list会循环list里面的元素再写入文件
# nwe_namers = '\n'.join(namers)   #h换行写入
# for index in range(len(nambers))
#     nambers
# f.writelines(nwe_namers)
# print(result)
# f.close()
# result = f.read()
# result = f.readlines()
# result = f.readline()
# print(result)

# result =f.write('acv')  #直接写在文件末尾
# result =f.writelines('acv')
'''
 总结：r只能读不能写
       w只能写不能读,w写入的文件不可读
       a能写能读
'''
#a+不能读可写(不能读是因为文件指针在末尾)
# f = open('a', 'a+',encoding='utf-8')
# # result = f.read()
# # print(result)
# result =f.write('acv')

#r+可读，读文件不存在时提示找不到改文件，写文件不存在时提示找不到改文件,不可写
# f = open('q.txt', 'r+',encoding='utf-8')
# result = f.read()
# print(result)
# result =f.write('acv')

#w+（不可读因为文件指针在末尾），读文件不存在时创建一个新的文件并且有可读权限,写文件会清空原文件内容，写不存在文件时创建一个新文件并且写入内容
# f = open('l.txt', 'w+',encoding='utf-8')
# result = f.read()
# print(result)
# result =f.write('acv')

# 文件指针：用于记录文件在哪一行

f = open('a', 'a+',encoding='utf-8')
f.seek(0)
result = f.read()
new_result = result.upper()
f.seek(0)
f.truncate()    #清空文件内容（清空文件内容从文件指针位置开始）
f.write(new_result)
f.close()