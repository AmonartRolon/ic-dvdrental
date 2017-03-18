from app import db

class Category(db.Model):

    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(20), nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Name: {0}>".format(self.name)
