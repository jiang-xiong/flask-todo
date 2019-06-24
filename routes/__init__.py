from flask import (
    session,
)

from models.user import User
from models.base_model import db


def current_user():
    db.create_all()
    uid = session.get('user_id', '')
    u = User.one(id=uid)
    return u
