import flask
#轻量级的web开发框架
import tools
import json
server = flask.Flask(__name__)


@server.route('/login',methods=['post','get'])
def login():
    username = flask.request.values.get('username','')
    password = flask.request.values.get('password','')
    # print(flask.request.cookies.get('PHPSESSID'))
    # print('json',flask.request.json)
    # flask.json.get('xxxx')#如果入参是json类型的话，这么搞
    # flask.request.cookies.get('xxx')#获取cookie里面的数据
    # flask.request.headers.get('xx')
    # flask.request.files.get("xxx")#文件

    if username.strip() and password.strip():
        p = tools.my_md5(password)
        query_sql = 'select * from app_myuser where username= "%s" and passwd="%s";' % (username, p)
        if tools.execute_sql(query_sql):
            return json.dumps({'code': '0', 'msg': '登录成功','sessionid':'xxxx'},ensure_ascii=False)
        else:
            return json.dumps({'code': '-1', 'msg': '输入的用户名/密码错误'})
    else:
        return json.dumps({'code': '-1', 'msg': '不能为空'})

@server.route('/reg',methods=['post','get'])
def reg():
    username = flask.request.values.get('username')
    password = flask.request.values.get('password')
    cpassword = flask.request.values.get('cpassword')
    if username.strip() and password.strip() and cpassword.strip():
        if password.strip() != cpassword.strip():
            return json.dumps({'code': -1, 'msg': '两次输入的密码不一样'})
        else:
            sql='select * from app_myuser where username="%s";'%username
            if tools.execute_sql(sql):
                return json.dumps({'code':-1,'msg':'用户已经存在'})
            else:
                p = tools.my_md5(password)
                insert_sql = 'insert into app_myuser (username,passwd) value ("%s","%s");'%(username,p)
                tools.execute_sql(insert_sql)
                return json.dumps({'code':0,'msg':'注册成功！'},ensure_ascii=False)

    else:
        return json.dumps({'code':-1,'msg':'必填参数不能为空'})



server.run(host='0.0.0.0',port=8999,debug=True)


