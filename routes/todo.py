from flask import (
    render_template,
    url_for,
    Blueprint,
    request,
    redirect,
    jsonify,
)

from routes import current_user

from models.todo import Todo
from models.base_model import db


main = Blueprint('todo', __name__)


@main.route("/")
def index():
    u = current_user()
    ts = Todo.all(user_id=u.id)
    return render_template("todo.html", user=u, tasks=ts)


@main.route("/all")
def all_task():
    u = current_user()
    ts = Todo.all(user_id=u.id)
    response = []
    for t in ts:
        d = dict(
            id=t.id,
            task=t.task,
            done=t.done,
        )
        response.append(d)
    # print('response', response)
    return jsonify(response)


@main.route("/add", methods=['POST'])
def add_task():
    form = request.form
    print('form', form)
    Todo.add(form)
    response = dict(
        response='success to add task',
    )
    return jsonify(response)


@main.route("/delete/<int:id>")
def delete(id):
    Todo.delete(id)
    response = dict(
        response='success to delete task',
    )
    return jsonify(response)


@main.route("/done", methods=['POST'])
def done():
    id = request.form.get('id', 0)
    done = request.form.get('done', '0')
    Todo.update(id=id, done=done)
    response = dict(
        response='success to done task',
    )
    return jsonify(response)
