from flask_restful import Resource
import json
from helpers.payment import *
from flask import request


class PaymentApi(Resource):
    def post(self, route):
        if route == "createPayment":
            return CreatePayment()
    
    def get(self, route):
        if route == "readAllPayment":
            return GetAllPayment()
    
    def delete(self, route):
         if route == "deletePayment":
            return DeletePayment()
         
    def patch(self, route):
        if route == "updatePayment":
            return UpdatePayment()
        