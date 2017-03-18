from flask import render_template
from flask import Blueprint
from flask import url_for
from app.actors.models import Actor
from app import db

mod = Blueprint('actors', __name__, url_prefix = '/actors')

@mod.route('/browse')
def browse():
    actors = Actor.query.all()
    return render_template('actors/browse.html', actors = actors)

@mod.route('/<id>')
def actors(id):
    actor = Actor.query.get(id)
    return render_template('actors/actor.html', actor = actor)
