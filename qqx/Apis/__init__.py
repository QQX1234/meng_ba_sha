from flask_restful import Api

from qqx.Apis.BannerApi import BannerResource
from qqx.Apis.GoodApi import GoodResource
from qqx.Apis.LoginApi import Login
from qqx.Apis.RegisterApi import Register


api = Api()

def init_apis(tpc):
    api.init_app(tpc)


# 添加资源
api.add_resource(BannerResource,'/api/v1/banner/')
api.add_resource(GoodResource,'/api/v1/goods/')
api.add_resource(Register,'/api/v1/register/',endpoint='')
api.add_resource(Login,'/api/v1/login/')