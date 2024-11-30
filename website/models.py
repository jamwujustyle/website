from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime, timedelta


class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    # date = db.Column(db.DateTime(timezone=True), default=func.now)
    # deadline = db.Column(db.Date, default=datetime.utcnow().date() + timedelta(days=1))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(50))
    first_name = db.Column(db.String(50))
    tasks = db.relationship("Task")
