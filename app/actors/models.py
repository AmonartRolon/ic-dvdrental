from app import db

class Actor(db.Model):

    __tablename__ = 'actor'

    actor_id = db.Column(db.Integer, primary_key = True)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return "<First name: {0} Last name: {1}>".format(self.first_name,
                self.last_name)
