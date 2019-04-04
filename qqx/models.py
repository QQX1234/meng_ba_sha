
from qqx.ext import db

#用户表
class User(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    phone = db.Column(db.String(100),unique=True)
    password = db.Column(db.String(256))
    email = db.Column(db.String(40),unique=True)
    permissions = db.Column(db.Integer,default=1)
    icon = db.Column(db.String(256),default='logo1.jpg')
    isactive = db.Column(db.Boolean,default=False)
    isdelete = db.Column(db.Boolean,default=False)


# 轮播图
class Banner(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(256))



#商品列表
class Good(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    img = db.Column(db.String(256))