from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')

db = SQLAlchemy(app)

from app.films.views import mod as filmsModule
app.register_blueprint(filmsModule)

from app.countries.views import mod as countriesModule
app.register_blueprint(countriesModule)

from app.views import mod as mainModule
app.register_blueprint(mainModule)

from app.actors.views import mod as actorsModule
app.register_blueprint(actorsModule)

from app.categories.views import mod as categoriesModule
app.register_blueprint(categoriesModule)

from app.languages.views import mod as languagesModule
app.register_blueprint(languagesModule)

from app.stores.views import mod as storesModule
app.register_blueprint(storesModule)

from app.cities.views import mod as citiesModule
app.register_blueprint(citiesModule)

from app.users.views import mod as usersModule
app.register_blueprint(usersModule)
