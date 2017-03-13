from flask import render_template
from flask import Blueprint
from flask import url_for
from app.films.models import Film
from app import db

mod = Blueprint('films', __name__, url_prefix = '/films')

@mod.route('/browse')
def browse():
    films = Film.query.all()
    return render_template('films/browse.html', films = films)

@mod.route('/<id>')
def films(id):
    film = Film.query.get(id)
    return render_template('films/film.html', film = film)
