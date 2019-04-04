import os

from flask_bootstrap import Bootstrap
from flask_caching import Cache
from flask_mail import Mail
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from qqx.settings import BASE_DIR

db = SQLAlchemy()
migrate = Migrate()



cache = Cache(config={

    # filename
    "CACHE_TYPE": "filesystem",
    "CACHE_DIR": os.path.join(BASE_DIR,'cachedir')

#     # redis
#       "CACHE_TYPE": "redis",
      # "CACHE_KEY_PREFIX": "flask(cache)"
})

mail = Mail()


def init_ext(tpc):
    db.init_app(tpc)
    migrate.init_app(app=tpc,db=db)


    Bootstrap(tpc)

    cache.init_app(tpc)
    mail.init_app(tpc)
