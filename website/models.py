import time
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    username = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    note = db.relationship('Note')
    created_at = db.Column(
        db.DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = db.Column(
        db.DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S"))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    discription = db.Column(db.String(1000))
    detail = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    created_at = db.Column(
        db.DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S"))
    updated_at = db.Column(
        db.DateTime, default=time.strftime("%Y-%m-%d %H:%M:%S"))
