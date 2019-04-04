import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'SDNKJHAIUSHFAOK%AS$SD&JF'

class DevelopConfig(BaseConfig):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123456@127.0.0.1:3306/python18120329'

    # 邮箱配置
    MAIL_SERVER = 'smtp.qq.com'
    MAIL_USERNAME = '976393191@qq.com'
    MAIL_PASSWORD = 'miwymbgsirolbfei'


config={
    'develop':DevelopConfig,
    'default':DevelopConfig,
}

def init_app(qqx,env_name):
    qqx.config.from_object(config.get(env_name))