from flask import render_template
from flask import Blueprint
from flask import url_for
from app.cities.models import City
from app import db

mod = Blueprint('cities', __name__, url_prefix = '/cities')

@mod.route('/browse')
def browse():
    cities = City.query.all()
    return render_template('cities/browse.html', cities = cities)

@mod.route('/<id>')
def cities(id):
    city = City.query.get(id)
    return render_template('cities/city.html', city = city)
