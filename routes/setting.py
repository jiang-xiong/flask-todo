import os
import uuid

from flask import (
    render_template,
    url_for,
    Blueprint,
    request,
    redirect,
)

from werkzeug.datastructures import FileStorage

from models.user import User

from routes import current_user

main = Blueprint('setting', __name__)


@main.route("/")
def index():
    u = current_user()
    return render_template("setting.html", user=u)


@main.route('/add', methods=['POST'])
def add_avatar():
    file: FileStorage = request.files['avatar']
    suffix = file.filename.split('.')[-1]
    filename = '{}.{}'.format(str(uuid.uuid4()), suffix)
    path = os.path.join('static/img', filename)
    file.save(path)

    u = current_user()
    User.update(u.id, image='/static/img/{}'.format(filename))

    return redirect(url_for('todo.index'))
