from app import db

class Film(db.Model):

    __tablename__ = 'film'

    film_id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(255), nullable = False)
    description = db.Column(db.Text, nullable = False)
    release_year = db.Column(db.Text, nullable = False)
    language_id = db.Column(db.Integer, nullable = False)
    rental_duration = db.Column(db.Integer, nullable = False)
    rental_rate = db.Column(db.Numeric, nullable = False)
    length = db.Column(db.Integer, nullable = False)
    replacement_cost = db.Column(db.Numeric, nullable = False)
    rating = db.Column(db.Text)
    last_update = db.Column(db.TIMESTAMP, nullable = False)
    special_features = db.Column(db.Text)
    fulltext = db.Column(db.Text)

    def __init__(self, title, description, release_year, language_id,
            rental_duration, rental_rate, length, replacement_cost):
        self.title = title
        self.description = description
        self.release_year = release_year
        self.language_id = language_id
        self.rental_duration = rental_duration
        self.rental_rate = rental_rate
        self.length = length
        self.replacement_cost = replacement_cost

    def __repr__(self):
        return "<Title: {0} Description: {1} \
            Release Year: {2}>".format(self.title, self.description, self.release_year)
