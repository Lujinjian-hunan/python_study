import base64

#加密
s='dgsdgs2323t牛寒阳'
r = base64.b64encode(s.encode())
result = r.decode()
print(result)

#解密
r = base64.b64decode('bGl1aGFpeWFuZzI2NjIzQDQyJCMj5Lit5paH')
print(r.decode())

#