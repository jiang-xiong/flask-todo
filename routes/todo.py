from flask import (
    render_template,
    url_for,
    Blueprint,
    request,
    redirect,
)

from routes import current_user

from models.todo import Todo

main = Blueprint('todo', __name__)


@main.route("/tasks")
def index():
    u = current_user()
    ts = Todo.all(u_id=u.id)
    return render_template("todo.html", user=u, tasks=ts)
