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
