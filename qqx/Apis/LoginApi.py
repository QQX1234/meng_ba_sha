# 请求定制
import time
import uuid

from flask import render_template
from flask_mail import Message
from flask_restful import reqparse, fields, Resource, marshal_with
from werkzeug.security import check_password_hash
from qqx.ext import mail,cache

from qqx.models import User

parser = reqparse.RequestParser()
parser.add_argument('phone',type=str,required=True,help='请提供手机号码')
parser.add_argument('password',type=str,required=True,help='请输入密码')





# 响应格式定制

#自定义属性
class IconFormat(fields.Raw):
    def format(self, value):
        return '/static/images/' +value



user_fields = {
        'username' : fields.String,
        'icon' : IconFormat(attribute='icon'),    #自定义属性
        'permissions' : fields.Integer,
    }


result_fields = {
    'msg' : fields.String,
    'status' : fields.Integer,
    'date' : fields.String,
    'user' : fields.Nested(user_fields),
    'token' : fields.String,
}


#定义资源
class Login(Resource):
    @marshal_with(result_fields)
    def post(self):
        # 用户
        parse = parser.parse_args()
        user = User()
        phone = parse.get('phone')
        password = parse.get('password')



        response_data = {
            'date' : str(time.time()),
            'status' : 406
        }


        # #数据处理
        # response_data['status'] = '406'
        # response_data['user'] = ''

        users = User.query.filter(User.phone == phone)
        if users.count():
            user = users.first()
            if check_password_hash(user.password, password):
                if user.isdelete:
                    response_data['msg'] = '登录失败，用户不存在'
                    return response_data


                token = uuid.uuid5(uuid.uuid4(),'register').hex
                cache.set(token,user.id,timeout=60*10)

                if user.isactive:
                    response_data['msg'] = '登录成功'
                    response_data['status'] = 200
                    response_data['user'] = user
                    response_data['token'] = token
                    return response_data

                else:

                    active_url = 'http://10.20.152.194:5000/api/v1/active/?token=' +token
                    tempplate_str = render_template('mail_active.html',active_url=active_url,phone=user.phone)
                    msg = Message(
                        subject='梦芭莎激活邮件',
                        sender='976393191@qq.com',
                        recipients=[user.email],
                        html=tempplate_str

                    )

                    mail.send(msg)

                    response_data['msg'] = '登录失败，用户未激活；激活邮件已发送，请注意查收'
                    return response_data

            else:
                response_data['msg'] = '登录失败，密码错误'
                return response_data
        else:
            response_data['msg'] = '登录失败，用户不存在'
            return response_data

