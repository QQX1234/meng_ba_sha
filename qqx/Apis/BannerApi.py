# 响应格式定制

"""
{
    'status': 200,
    'msg': '轮播图数据获取成功',
    'number': 4,
    'date': '456789t67896789',
    'list': [
        {
            'id': 1,
            'img': 'r56789t678',
            'name': 'xxx',
            'trackid': 'xxx'
        },
        ...
    ]
}
"""
import time
from flask_restful import marshal_with, Resource, fields

from qqx.models import Banner

banner_fileds = {
    'id': fields.Integer,
    'img': fields.String,
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'number': fields.Integer,
    'date': fields.String(default=str(time.time())),
    'list': fields.List(fields.Nested(banner_fileds))
}


class BannerResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        banners = Banner.query.all()

        responseData = {
            'status': 200,
            'msg': '获取轮播图数据成功',
            'number': len(banners),
            'list': banners
        }

        return responseData