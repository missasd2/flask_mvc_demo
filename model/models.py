# -*- coding: UTF-8 -*-
from database.exts import db

class User(db.Model):
    __tablename__='users'
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    username=db.Column(db.String(255), nullable=False)
    password=db.Column(db.String(255))

    # def __init__(self,username,password):
    #     self.name=username
    #     self.password=password
    #
    # def __repr__(self):
    #     return '<User {}>'.format(self.name)