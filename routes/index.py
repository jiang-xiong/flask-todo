from flask import (
    render_template,
    Blueprint,
    request,
    redirect,
    url_for,
    session,
)

from models.user import User

main = Blueprint('index', __name__)


@main.route("/")
def index():
    return render_template("index.html")


@main.route("/signup", methods=['POST'])
def signup():
    form = request.form
    User.signup(form)
    return redirect(url_for('index.index'))


@main.route("/login", methods=['POST'])
def login():
    form = request.form
    u = User.validate_login(form)
    if u is None:
        return redirect(url_for('index.index'))
    else:
        session['user_id'] = u.id
        session.permanent = True
        return redirect(url_for('todo.index'))
