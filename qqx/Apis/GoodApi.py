import time
from flask_restful import marshal_with, Resource, fields

from qqx.models import Banner, Good

good_fileds = {
    'id': fields.Integer,
    'img': fields.String,
}

result_fields = {
    'status': fields.Integer,
    'msg': fields.String,
    'number': fields.Integer,
    'date': fields.String(default=str(time.time())),
    'list': fields.List(fields.Nested(good_fileds))
}


class GoodResource(Resource):
    @marshal_with(result_fields)
    def get(self):

        goods = Good.query.all()

        responseData = {
            'status': 200,
            'msg': '获取商品数据成功',
            'number': len(goods),
            'list': goods
        }

        return responseData