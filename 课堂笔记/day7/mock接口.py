import fastapi
from fastapi import Form
from starlette.requests import Request

import uvicorn
import tools
server = fastapi.FastAPI()
# pip install python-multipart

# @server.post('/login')
# def login(request:Request,username:str=Form(...),password:str=Form(...)):
#     return {'username':username,'password':password}


@server.get('/login')
def login(username: str, password: str):
    if username.strip() and password.strip():
        p = tools.my_md5(password)
        query_sql = 'select * from app_myuser where username= "%s" and passwd=%s;' % (username, p)
        if tools.excute(query_sql):
            return {'code': '0', 'msg': '登录成功'}
        else:
            return {'code': '-1', 'msg': '输入的用户名/密码错误'}
    else:
        return {'code': '-1', 'msg': '不能为空'}

@server.get('/product')
def test():
    return {
        'code':0,
        'data':[
            {'product_name':'朝朝盈1号','status':0},
            {'product_name':'朝朝盈2号','status':2},
            {'product_name':'朝朝盈2号','status':1},
            {'product_name':'朝朝盈2号','status':0}
        ]
    }


@server.get('/pay')
def pay(money:float,status='1'):
    if status=='0':
        return {'code':1,'status':'fail'}
    elif status=='1':
        return {'code':0,'status':'success','balance':money}

@server.post('/reg')
def reg(username:str,password:str,cpassword:str):
    if username.strip() and password.strip() and cpassword.strip():
        if password.strip() != cpassword.strip():
            return {'code': -1, 'msg': '两次输入的密码不一样'}
        else:
            sql='select * from app_myuser where username="%s";'%username
            if tools.execute_sql(sql):
                return {'code':-1,'msg':'用户已经存在'}
            else:
                p = tools.my_md5(password)
                insert_sql = 'insert into app_myuser (username,passwd) value ("%s","%s");'%(username,p)
                tools.execute_sql(insert_sql)
                return {'code':0,'msg':'注册成功！'}

    else:
        return {'code':-1,'msg':'必填参数不能为空'}



uvicorn.run(server,port=8888,debug=True,host='0.0.0.0')
# http://127.0.0.1:8888/product
# http://192.168.1.xx:8888/product
