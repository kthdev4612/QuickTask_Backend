from flask_restful import Resource
import json
from helpers.booking import *
from flask import request


class BookingApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateUser()
    
    def get(self, route):
        if route == "read":
            return ReadUser()
    
    def delete(self, route):
         if route == "delete":
            return DeleteUser()
         
    def patch(self, route):
        if route == "update":
            return UpdateUser()
        