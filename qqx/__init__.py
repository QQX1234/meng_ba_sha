from qqx.Apis import init_apis
from qqx.ext import init_ext
from qqx.settings import init_app
from qqx.views import init_blue


def create_app(env_name='default'):
    from flask import Flask

    qqx = Flask(__name__)

    init_app(qqx, env_name)

    init_ext(qqx)

    init_blue(qqx)

    init_apis(qqx)

    return qqx


