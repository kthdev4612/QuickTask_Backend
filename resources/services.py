from flask_restful import Resource
import json
from helpers.services import *
from flask import request


class ServicesApi(Resource):
    def post(self, route):
        if route == "create":
            return CreateService()
    
    def get(self, route):
        if route == "readall":
            return ReadAllService()
        if route == "readsingle":
            return ReadSingleService()
    
    def delete(self, route):
         if route == "delete":
            return DeleteService()
         
    def patch(self, route):
        if route == "update":
            return UpdateService()
        