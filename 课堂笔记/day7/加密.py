import hashlib

s = 'huoziyang123' + 'sd23$@#%G@#25'#盐
s = s.encode()
m = hashlib.sha384(s) #bytes,不可逆
result = m.hexdigest()

def my_md5(s):
    s = str(s)
    s = s.encode()
    m = hashlib.md5(s)  # bytes,不可逆
    result = m.hexdigest()
    return result

print(result)

#同样的字符串，md5出来的结果都一样
#niuhanyang 123456
#niuhanyang 0da0c4db92c8c7b83e93218533fa26f6
#加盐
#撞库