from application import db

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item = db.Column(db.String(75), nullable=False)
    chemical = db.Column(db.Boolean, nullable = False, default=False)
    #quantity = db.Column(db.Integer, nullable=False)
    #units = db.Column(db.String(10), nullable = False)
