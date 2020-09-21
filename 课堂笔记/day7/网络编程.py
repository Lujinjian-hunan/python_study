#做接口自动化

#python自带的模块
from urllib import request
from urllib.parse import urlencode
import requests
import json


#开发好了一个接口  server

#请求接口  client

# url = 'http://127.0.0.1:8999/login?username=niuhanyang2&password=1'
# req = request.urlopen(url)#get请求
#
# dic = json.loads(req.read().decode())


# print(urlencode(data))
# req = request.urlopen(url,urlencode(data).encode())
#
# dic = json.loads(req.read().decode())
# print(dic)

url = 'http://127.0.0.1:8999/login'
data = {'username':'niuhanyang2','password':'1'}
#get、post、传cookie、headers、传文件、传json、下载文件

#get请求
# r = requests.get(url,data)
#Cookie:

cookie  = {'wp-settings-1':'1','PHPSESSID':'xxxxx'}
headers = {
    'user-agent':'xxxx',
    'cookie':'wp-settings-1=libraryContent%3Dbrowse%26posts_list_mode%3Dexcerpt%26editor%3Dtinymce%26post_dfw%3Doff%26imgsize%3Dfull%26editor_plain_text_paste_warning%3D1%26hidetb%3D1; wp-settings-time-1=1573143656; comment_author_8ec14a05b6903cd9021ece26c7b908a0=111; PHPSESSID=2e33445700b8381f67cafb40ee147480'}
# r = requests.post(url,data=data,params={"version":1.0},cookies=cookie)#
# r = requests.post(url,data=data,params={"version":1.0},headers=headers)
#params是把参数传到url后头的

# r = requests.post(url,json=data)

# url = 'http://api.nnzhp.cn/api/file/file_upload'
# data = {'file':open('shuaige.xls','rb')}
# r = requests.post(url,files=data)
r = requests.get('https://ss2.bdstatic.com/70cFvnSh_Q1YnxGkpoWK1HF6hhy/it/u=293407302,1362956882&fm=26&gp=0.jpg',verify=False)


# print(r.json() ) #->字典  #d.get('')
# print(r.text) #字符串格式
print(r.content) #bytes类型的

f = open('a.jpg','wb')
f.write(r.content)
f.close()
print(r.status_code) #返回的状态码