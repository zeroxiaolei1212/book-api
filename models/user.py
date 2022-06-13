from db import db
import base64
from flask import current_app

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(128))
    email = db.Column(db.String(64), unique=True)
    nickname = db.Column(db.String(32))
    birthday = db.Column(db.DateTime())
    avatar = db.Column(db.Text())

    def __init__(self, username, password,email,nickname,birthday,avatar):
        self.username = username
        self.password = base64.b64encode(password.encode('utf8'))
        self.email = email
        self.nickname = nickname
        self.birthday = birthday
        self.avatar = avatar if avatar else current_app.config['DEFAULT_AVATAR']

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()
    
    @classmethod
    def find_by_login(cls, username, password):
        return cls.query.filter_by(username=username, password=base64.b64encode(password.encode('utf8'))).first()
    
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id = id).first()
    
    @classmethod
    def update_by_userinfo(cls, id, email, nickname, birthday, avatar):
        user = cls.query.filter_by(id = id).first()
        user.email = email
        user.nickname = nickname
        user.birthday = birthday
        user.avatar = avatar
        db.session.commit()