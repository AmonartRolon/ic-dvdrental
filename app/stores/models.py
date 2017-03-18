from app import db

class Store(db.Model):

    __tablename__ = 'store'

    store_id = db.Column(db.Integer, primary_key = True)
    manager_staff_id = db.Column(db.Integer, nullable = False)
    address_id = db.Column(db.Integer, nullable = False)
    last_update = db.Column(db.TIMESTAMP, nullable = False)

    def __init__(self, manager_staff_id, address_id):
        self.manager_staff_id = manager_staff_id
        self.address_id = address_id

    def __repr__(self):
        return "<Store number: {0} Address:{1}>".format(self.store_id, self.address_id)
