import datetime
from config.db import *
from sqlalchemy.sql import expression


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    Username = db.Column(db.String(128), nullable=False)
    Email = db.Column(db.String(128), nullable=False)
    Password = db.Column(db.String(128), nullable=False)
    Mobile = db.Column(db.String(128), nullable=False)
    Address = db.Column(db.String(128), nullable=False)
    Country = db.Column(db.String(128), nullable=False)
    City = db.Column(db.String(128), nullable=False)


class Service_Provider(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.id'))
    Service_details = db.Column(db.String(128), nullable=False)


class Services(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ServiceName = db.Column(db.String(128), nullable=False)
    Description = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.String(128), nullable=False)
    ProviderID = db.Column(db.Integer, db.ForeignKey('Service_Provider.id'))


class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.id'))
    ServiceID = db.Column(db.Integer, db.ForeignKey('Services.id'))
    BookingDate = db.Column(db.String(128), nullable=False)
    Status = db.Column(db.String(20), nullable=False)

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    UserID = db.Column(db.Integer, db.ForeignKey('User.id'))
    BookingID = db.Column(db.Integer, db.ForeignKey('Booking.id'))
    Amount = db.Column(db.String(128), nullable=False)
    PaymentDate = db.Column(db.String(20), nullable=False)



