from flask import render_template
from flask import Blueprint
from flask import url_for
from app.stores.models import Store
from app import db

mod = Blueprint('stores', __name__, url_prefix = '/stores')

@mod.route('/browse')
def browse():
    stores = Store.query.all()
    return render_template('stores/browse.html', stores = stores)

@mod.route('/<id>')
def stores(id):
    store = Store.query.get(id)
    return render_template('stores/store.html', store = store)
