from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import (
    Column,
    Integer,
    String,
)

db = SQLAlchemy()


class SQLMixin(object):
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)

    # 接收一个字典写入数据库
    @classmethod
    def new(cls, form):
        m = cls()
        for name, value in form.items():
            setattr(m, name, value)
        db.session.add(m)
        db.session.commit()

    # 从数据库找第一个符合条件的用户
    @classmethod
    def one(cls, **kwargs):
        ms = cls.query.filter_by(**kwargs).first()
        return ms

    @classmethod
    def add(cls, form):
        cls.new(form)

    @classmethod
    def all(cls, **kwargs):
        ms = cls.query.filter_by(**kwargs).all()
        return ms

    @classmethod
    def delete(cls, id):
        m = cls.query.filter_by(id=id).first()
        db.session.delete(m)
        db.session.commit()

    @classmethod
    def update(cls, id, **kwargs):
        m = cls.query.filter_by(id=id).first()
        for name, value in kwargs.items():
            setattr(m, name, value)

            db.session.add(m)
            db.session.commit()
