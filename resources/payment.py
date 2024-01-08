from flask_restful import Resource
import json
from helpers.payment import *
from flask import request


class PaymentApi(Resource):
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
        