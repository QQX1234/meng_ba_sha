from flask import Blueprint, request, render_template
from qqx.ext import cache,db
from qqx.models import User

blue = Blueprint('blue',__name__)

def init_blue(qqx):
    qqx.register_blueprint(blueprint=blue)



@blue.route('/index/')
def index():

    return render_template('index.html')


@blue.route('/api/v1/active/')
def active():
    if request.method == 'GET':
        token = request.args.get('token')
        userid = cache.get(token)


        try:
            user = User.query.get(userid)
            user.isactive = True
            db.session.add(user)
            db.session.commit()

            return render_template('active.html')

        except:
            return '激活失败，已超时'
