from app import db

class User(db.Model):
    __tablename__ = 'customer'

    customer_id = db.Column(db.Integer, primary_key = True)
    store_id = db.Column(db.Integer, nullable = False)
    first_name = db.Column(db.String(45), nullable = False)
    last_name = db.Column(db.String(45), nullable = False)
    email = db.Column(db.String(50), unique = True)
    password = db.Column(db.String(120))
    role = db.Column(db.Integer)
    address_id = db.Column(db.Integer, nullable = False)
    activebool = db.Column(db.Boolean, nullable = False)
    create_date = db.Column(db.Date, nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)
    active = db.Column(db.Integer, nullable = False)

    def __init__(self, store_id, first_name, last_name, email, address_id):
        self.store_id = store_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address_id = address_id

    def __repr__(self):
        return "<Name: {0}, Email: {1}>".format(self.first_name, self.email)

