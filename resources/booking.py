from flask_restful import Resource
import json
from helpers.booking import *
from flask import request


class BookingApi(Resource):
    def post(self, route):
        if route == "createBooking":
            return CreateBooking()
    
    def get(self, route):
        if route == "ReadAllBooking":
            return GetAllBooking()

        if route == "readSingleBooking":
            return GetSingleBooking()
    
    def delete(self, route):
         if route == "DeleteBooking":
            return DeleteBooking()
         
    def patch(self, route):
        if route == "UpdateBooking":
            return UpdateBooking()
        