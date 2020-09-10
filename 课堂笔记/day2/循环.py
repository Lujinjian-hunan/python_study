#重复做一件事情
#循环、迭代、遍历
# break  循环里面遇到break立即结束
# continue  循环里面遇到continue,结束本次循环

#while循环
# count = 0 #计数器
# rate = 140 #心率
# while count < 10:
#     count = count +1
#     if rate > 160:
#         rate -=10
#         # break
#         continue
#     print('跑圈', count)
#     rate += 5 #rate = rate +5

# for循环
# rate = 130
# for i in range(10):
#     print('跑圈',i,rate)
#     rate += 5
#     if rate == 160:
#         print('你的心跳太快了，强制休息')
#         break
#     rate += 5


# for i in range(10):
#     print(i)
#     if i ==8:
#         break
# else:
#     print('什么时候会执行这里的代码呢')

# count = 10
# while count > 0:
#     print(count)
#     if count == 2:
#         break
#     count -= 1#count = coubt -1
# else:
#     print('什么时候会执行这里的代码呢')