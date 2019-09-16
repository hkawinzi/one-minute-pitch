from . import db

class User(db.Model):
    __tablename__ = 'seconds'
    id = db.Column(db.Interger,primary_key = True)
    username = db.Column(db.String(255))
    