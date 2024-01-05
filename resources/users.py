from flask_restful import Resource
from helpers.users import *
from flask import request


class UsersApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateUser()
    
    def get(self, route):
        if route == "read":
            return ReadUser()
        
    def put(self, route):
        if route == "update":
            return UpdateUser()
    
    def delete(self, route):
         if route == "delete":
            return "True"
         
    def patch(self, route):
        if route == "CreateUser":
            return "True"
        