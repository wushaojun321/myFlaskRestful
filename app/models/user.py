# encoding:utf8
__auth__ = 'wsj'
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
from . import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(24), unique=True, nullable=False)
    nickname = db.Column(db.String(24), unique=True)
    auth = db.Column(db.SmallInteger, default=1)
    _password = db.Column('password', db.String(100))

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        print 1
        u = User(nickname=nickname, email=account, password=secret)
        db.session.add(u)
        db.session.commit()

