from app import db

class Country(db.Model):

    __tablename__  = 'country'

    country_id = db.Column(db.Integer, primary_key = True)
    country = db.Column(db.String(50), nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __init__(self, country):
        self.country = country

    def __repr__(self):
        return "Name: {0}".format(self.country)
