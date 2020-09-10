import random
num = input('请输入你要生成的双色球条目数：').strip()


# 判断输入的是否为大于的整数
def your_num(s):
    if s:
        if s.isdigit():
            if int(s) > 0:
                return int(s)
            else:
                print('请输入大于0的整数')
                return False
        else:
            print('请输入大于0的整数')
            return False
    else:
        print('输入不能为空')
        return False


def get_ball():
    n = your_num(num)
    for i in range(n):
        # 生成红色球,球的数字在1-33之间
        red_ball = random.sample(range(1, 34), 6)
        # 给红色球排序
        all_ball = sorted(red_ball)
        # 生成蓝色球,球的数字在1-16之间
        blue = random.randint(1, 17)
        # 加入蓝球
        all_ball.append(blue)
        # 格式化列表中的数字，个位数左边补零
        l = []
        for x in all_ball:
            d = '{:0>2d}'.format(x)
            l.append(d)
        l_str = ', '
        print(l_str.join(l))


get_ball()
