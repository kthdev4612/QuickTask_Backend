import datetime
from config.db import *
from sqlalchemy.sql import expression


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_username = db.Column(db.String(128), nullable=False)
    user_email = db.Column(db.String(128), nullable=False)
    user_password = db.Column(db.String(128), nullable=False)
    user_mobile = db.Column(db.String(128), nullable=False)
    user_address = db.Column(db.String(128), nullable=False)
    user_country = db.Column(db.String(128), nullable=False)
    user_city = db.Column(db.String(128), nullable=False)


class Service_Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    sp_userID = db.Column(db.Integer, db.ForeignKey(User.id))
    sp_service_details = db.Column(db.String(128), nullable=False)


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    s_serviceName = db.Column(db.String(128), nullable=False)
    s_description = db.Column(db.String(255), nullable=False)
    s_price = db.Column(db.String(128), nullable=False)
    s_providerID = db.Column(db.Integer, db.ForeignKey(Service_Provider.id))


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    b_userID = db.Column(db.Integer, db.ForeignKey(User.id))
    b_serviceID = db.Column(db.Integer, db.ForeignKey(Services.id))
    b_bookingDate = db.Column(db.String(128), nullable=False)
    b_status = db.Column(db.String(20), nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    p_userID = db.Column(db.Integer, db.ForeignKey(User.id))
    p_bookingID = db.Column(db.Integer, db.ForeignKey(Booking.id))
    p_amount = db.Column(db.String(128), nullable=False)
    p_paymentDate = db.Column(db.String(20), nullable=False)


