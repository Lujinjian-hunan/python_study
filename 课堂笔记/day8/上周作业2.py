import flask
import tools
import json
import time
import uuid
server = flask.Flask(__name__)

@server.route('/login',methods=['post','get'])
def login():
    username = flask.request.values.get('username','')
    password = flask.request.values.get('password','')
    if username.strip() and password.strip():
        p = tools.my_md5(password)
        query_sql = 'select * from app_myuser where username= "%s" and passwd="%s";' % (username, p)
        user_result = tools.execute_sql(query_sql)
        if user_result:
            session_str = '%s%s%s'%(username,time.time(),uuid.uuid4())
            session_id = tools.my_md5(session_str)
            user_id = user_result.get('id')
            tools.redis_str(session_id,'{"user_id":%s,"username":"%s"}' % (user_id,username) ,600)
            return json.dumps({'code': '0', 'msg': '登录成功','sessionid':session_id},ensure_ascii=False)
        else:
            return json.dumps({'code': '-1', 'msg': '输入的用户名/密码错误'})
    else:
        return json.dumps({'code': '-1', 'msg': '不能为空'})




@server.route('/pay',methods=['post','get'])
def pay():
    tools.logger.debug('进入支付接口')
    sessionid = flask.request.values.get('sessionid','')
    money = float(flask.request.values.get('money'))
    tools.logger.debug('请求参数:{}',flask.request.values)

    session = tools.check_session(sessionid)
    if session:
        user = json.loads(session)
        user_id = user.get('user_id')
        sql = 'select balance from app_myuser where id = %s;'%user_id
        tools.logger.debug('sql语句：{}',sql)
        balance = tools.execute_sql(sql).get('balance')
        if balance>=money:
            update_money = 'update app_myuser set balance = balance - %s where id = %s;' %(money,user_id)
            tools.execute_sql(update_money)
            return json.dumps({'code': 0, 'msg': '支付成功'},ensure_ascii=False)
        else:
            return json.dumps({'code': -1, 'msg': '余额不足'},ensure_ascii=False)
    else:
        return json.dumps({'code': 899, 'msg': '请登录！'},ensure_ascii=False)


if __name__ == '__main__':
    server.run(port=8888,debug=True)

