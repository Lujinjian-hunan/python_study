
# f = open('user.txt')
# f.close()

# with open('user.txt',encoding='utf-8') as f: #文件对象，文件句柄
#     for line in f:
#         print(line)
#         line = line.strip()
#         if line:
#             print(line)

#1、读取到文件所有内容
#2、替换 new_str
#3、清空原来的文件
#4、写进去新的


#新的
import os
# 打开a文件，再以只写的方式新建一个新文件
with open('words.txt') as fr,open('words_new.txt','w') as fw:
    for line in fr:
        line = line.strip()
        if line:
            # 把读取到的内容替换成大写再写入新文件中
            line = line.upper()
            fw.write(line+'\n')
# 用os模块的方法删除原文件再把新文件重命名为a
os.remove('words.txt')
os.rename('words_new.txt','words.txt')
