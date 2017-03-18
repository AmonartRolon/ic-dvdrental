from flask import render_template
from flask import Blueprint
from flask import url_for
from app.users.models import User
from app import db

mod = Blueprint('users', __name__, url_prefix = '/users')

@mod.route('/browse')
def browse():
    users = User.query.all()
    return render_template('users/browse.html', users = users)

@mod.route('/<id>')
def users(id):
    user = User.query.get(id)
    return render_template('users/user.html', user = user)
