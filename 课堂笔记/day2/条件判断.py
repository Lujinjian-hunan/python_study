score = input('请输入你的分数：')#input里面接收到的是str类型
score = int(score)
print('score的值===',score)
print('score的类型',type(score))
if score >= 90: #if写完之后要加冒号
    print('优秀')
elif score < 90 and score >= 75:
    print('良好')
elif score >= 60 and score <75:
    print('及格')
else:
    print('不及格')
if score ==90:
    print('猜对了')

if score !=83:
    print('不等于83')
# > < >= != ==
