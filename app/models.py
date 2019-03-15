from datetime import datetime

from app import db

class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column (db.Integer, primary_key=True)
    name = db.Column (db.String (64), unique=True)
    default = db.Column (db.Boolean, default=False, index=True)
    permissions = db.Column (db.Integer)
    user = db.relationship ('User', backref='role', lazy='dynamic')

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column (db.Integer, primary_key=True)
    email = db.Column (db.String (64), unique=True, index=True)
    username = db.Column (db.String (64), unique=True, index=True)
    role_id = db.Column (db.Integer, db.ForeignKey ('roles.id'))
    password_hash = db.Column (db.String (128))
    name = db.Column (db.String (64))
    location = db.Column (db.String (64))
    about_me = db.Column (db.Text ())
    member_since = db.Column (db.DateTime (), default=datetime.utcnow)
    last_seen = db.Column (db.DateTime (), default=datetime.utcnow)
    avatar_hash = db.Column (db.String (32))
    posts = db.relationship ('Post', backref='author', lazy='dynamic')