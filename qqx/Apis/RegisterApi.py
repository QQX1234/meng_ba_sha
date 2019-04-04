# 请求定制
import time
import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import reqparse, fields, Resource, marshal_with

from qqx.ext import mail, db,cache
from qqx.models import User

parser = reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True,help='请提供手机号码')
parser.add_argument('password',type=str,required=True,help='请输入密码')
parser.add_argument('email',type=str,required=True,help='请输入邮箱')




# 响应格式示例
"""
{
    'msg' : '注册成功',
    'status' : 200,
    'date' : 'xxxx',
    'data' : {
        'phone' : '15879764436',
        'icon' : '/static/images/logo1.jpg/',
        'permissions' : 1,
    },
    'token' : 'xxxxxx',
}
"""

# 响应格式定制

#自定义属性
class IconFormat(fields.Raw):
    def format(self, value):
        return '/static/images/' +value



user_fields = {
        'phone' : fields.String,
        'icon' : IconFormat(attribute='icon'),    #自定义属性
        'permissions' : fields.Integer,
    }


result_fields = {
    'msg' : fields.String,
    'status' : fields.Integer,
    'date' : fields.String,
    'user' : fields.Nested(user_fields,default={}),
    'token' : fields.String,
}


#定义资源
class Register(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 用户
        parse = parser.parse_args()
        user = User()
        user.phone = parse.get('phone')
        user.password = parse.get('password')
        user.email = parse.get('email')


        response_data = {
            'date' : str(time.time()),
        }


        #数据处理
        response_data['status'] = '406'
        response_data['user'] = ''

        users = User.query.filter(User.phone == user.phone)
        if users.count():
            response_data['msg'] = '该用户名已经存在，注册失败'
            return response_data

        users = User.query.filter(User.email == user.email)
        if users.count():
            response_data['msg'] = '邮箱已存在，注册失败'
            return response_data

        # 存入数据库
        db.session.add(user)
        db.session.commit()

        token = uuid.uuid5(uuid.uuid4(),'regisger').hex
        cache.set(token,user.id,timeout=60*3)

        active_url = 'http://10.20.152.194:5000/api/v1/active/?token=' +token
        tempplate_str = render_template('mail_active.html',active_url=active_url,phone=user.phone)
        msg = Message(
            subject='梦芭莎激活邮件',
            sender='976393191@qq.com',
            recipients=[user.email],
            html=tempplate_str

        )

        mail.send(msg)


        # 返回数据
        response_data['msg'] = '注册成功'
        response_data['status'] = 200
        response_data['user'] = user
        response_data['token'] = token

        return response_data