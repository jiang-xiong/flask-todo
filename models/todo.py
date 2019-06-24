from sqlalchemy import Column, String, Integer

from models.base_model import SQLMixin, db


class Todo(SQLMixin, db.Model):
    task = Column(String(50), nullable=False)
    u_id = Column(Integer, nullable=False)
