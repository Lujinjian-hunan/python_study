#判断小数

#'1.5'


def is_float(s):
    s =  str(s)
    if s.count('.') == 1: #1.3
        left,right = s.split('.')
        if left.isdigit() and right.isdigit():#正小数
            return True
        if left.startswith('-') and left.lstrip('-').isdigit() and right.isdigit():
            return True
    else:
        print('错误')

# print(is_float('-1.21'))
# print(is_float('1.2s'))
# print(is_float('s.3'))
# print(is_float('--1.3'))
# print(is_float( .3 ))#0.3
# print(is_float( '.3' ))#0.3
#函数里面遇到return，函数立即结束

is_float('as')
