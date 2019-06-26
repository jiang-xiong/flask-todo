from flask import Flask

from routes.index import main as index_routes
from routes.todo import main as todo_routes
from routes.setting import main as setting_routes

from models.base_model import db


def register_routes(app):
    app.register_blueprint(index_routes)
    app.register_blueprint(todo_routes, url_prefix='/todo')
    app.register_blueprint(setting_routes, url_prefix='/setting')


def configured_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)


# 配置 app，数据库，注册路由
def configured_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.secret_key = 'string'

    register_routes(app)
    configured_db(app)

    return app


if __name__ == '__main__':
    app = configured_app()

    config = dict(
        debug=True,
        host='localhost',
        port=2000,
        threaded=True,
    )
    app.run(**config)
