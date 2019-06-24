from sqlalchemy import Column, String

from models.base_model import SQLMixin, db


class User(SQLMixin, db.Model):
    username = Column(String(50), nullable=False)
    password = Column(String(256), nullable=False)
    image = Column(String(100), nullable=False, default='/static/img/default.jpg')

    # 把的注册用户写入数据库
    @classmethod
    def signup(cls, form):
        db.create_all()
        User.new(form)

    # 返回第一个符合用户名，密码的用户
    @classmethod
    def validate_login(cls, form):
        query = dict(
            username=form['username'],
            password=form['password'],
        )
        return User.one(**query)

