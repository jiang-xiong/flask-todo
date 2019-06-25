from sqlalchemy import Column, String, Integer, Boolean

from models.base_model import SQLMixin, db


class Todo(SQLMixin, db.Model):
    task = Column(String(50), nullable=False)
    user_id = Column(Integer, nullable=False)
    done = Column(String(50), nullable=False, default='0')
