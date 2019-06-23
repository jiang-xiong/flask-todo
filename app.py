from flask import Flask

from routes.index import main as index_routes


def register_routes(app):
    app.register_blueprint(index_routes)


# 配置 app，数据库，注册路由
def configured_app():
    app = Flask(__name__)
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.jinja_env.auto_reload = True
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

    register_routes(app)

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
