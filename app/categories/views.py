from flask import render_template
from flask import Blueprint
from flask import url_for
from app.categories.models import Category
from app import db

mod = Blueprint('categories', __name__, url_prefix = '/categories')

@mod.route('/browse')
def browse():
    categories = Category.query.all()
    return render_template('categories/browse.html', categories = categories)

@mod.route('/<id>')
def categories(id):
    category = Category.query.get(id)
    return render_template('categories/category.html', category = category)
