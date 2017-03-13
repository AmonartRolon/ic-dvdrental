from flask import render_template
from flask import Blueprint
from flask import url_for
from app.countries.models import Country
from app import db

mod = Blueprint('countries', __name__, url_prefix = '/countries')

@mod.route('/browse')
def browse():
    countries = Country.query.all()
    return render_template('countries/browse.html', countries = countries)

@mod.route('/<id>')
def countries(id):
    country = Country.query.get(id)
    return render_template('countries/country.html', country = country)
