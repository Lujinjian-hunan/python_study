import json
# d = {'name':'xiaohei','cars':[1,2,3],'house':(4,5,6),
#      'addr':'北京','age':18,'sex':'男','money':100,'msg':'ok'}
# #json就是一个字符串，只不过是所有语言都能解析这个字符串
#
# result = json.dumps(d,ensure_ascii=False,indent=4) #pyton的数据类型转json的 #（list、tuple、dict）
#
# print(result)
# print(type(result))

# json_str = ' {"name": "xiaohei", "cars": [1, 2, 3], "house": [4, 5, 6]} '
# d = json.loads(json_str)
#
# print(d)
# print(type(json_str))
# print(type(d))

# content = f.read()
# d = json.loads(content)
#
# d = json.load(f) #帮你封装了处理文件的功能

#json_str = json.dumps(d,indent=4,ensure_ascii=False)
#f.write(json_str)

#json.dump(d,f,indent=4,ensure_ascii=False)

# hzy = [1,2,3,4]
# with open('info2.json','w',encoding='utf-8') as fw:
#     json.dump(hzy,fw,ensure_ascii=False,indent=4)

# user = {'name':'张三', 'age':18, 'sex':'男', 'hobby':'篮球'}
# with open('user.json','w',encoding='utf-8') as fw:
#     json.dump(user, fw, ensure_ascii=False, indent=4, sort_keys=True)
#
#
# with open('user.json',encoding='utf-8') as fr:
#     d = json.load(fr)
#     print(d)
#     print(d.get('name'))
#     print(d.get('age'))


L1 = [ { 'a' : 1, 'b' : 2, 'c' : 3, 'd' : 4, 'e' : 5 } ]

data = json.dumps(L1, ensure_ascii=False,indent=4, sort_keys=True)
print(data)
