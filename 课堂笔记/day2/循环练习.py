# 写一个小游戏；
# 猜数字的游戏
#     1、最多输入5次，如果猜的不对，提示它大了还是小了，猜对了游戏结束，如果次数用尽还没有猜对，提示已达到次数


import random
number = random.randint(1,100)
for i in range(5):
    guess = input('请输入你猜的数字：')
    guess = int(guess)
    if guess == number:
        print('恭喜你猜对了，游戏结束')
        break
    elif guess > number:
        print('猜大了')
        continue
    else:








        print('猜小了')
        continue
else:
    print('错误次数过多')