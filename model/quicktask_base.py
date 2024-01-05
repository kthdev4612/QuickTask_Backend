import datetime
from config.db import *
from sqlalchemy.sql import expression


class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)



