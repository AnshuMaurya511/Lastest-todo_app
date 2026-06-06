from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(500))
    email = db.Column(db.String(500), nullable=False)
    password = db.Column(db.String(1000), nullable=False)


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(1000))
    date_time = db.Column(db.String(200))
    work = db.Column(db.String(50), default="Pending")
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
