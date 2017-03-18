from app import db

class City(db.Model):

    __tablename__ = 'city'

    city_id = db.Column(db.Integer, primary_key = True)
    city = db.Column(db.String(50), nullable = False)
    country_id = db.Column(db.Integer, nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __init__(self, city, country_id):
        self.city = city
        self.country_id = country_id

    def __repr__(self):
        return "<City: {0} Country: {1}>".format(self.city, self.country_id)
