from flask import render_template
from flask import Blueprint
from flask import url_for
from app.languages.models import Language
from app import db

mod = Blueprint('languages', __name__, url_prefix = '/languages')

@mod.route('/browse')
def browse():
    languages = Language.query.all()
    return render_template('languages/browse.html', languages = languages)

@mod.route('/<id>')
def languages(id):
    language = Language.query.get(id)
    return render_template('languages/language.html', language = language)
