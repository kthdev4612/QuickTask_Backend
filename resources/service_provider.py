from flask_restful import Resource
import json
from helpers.service_provider import *
from flask import request


class Service_ProviderApi(Resource):
    def post(self, route):
        if route == "createServiceProvider":
            return CreateSp()
    
    def get(self, route):
        if route == "readServiceProvider":
            return GetAllSp()
    
    def delete(self, route):
         if route == "deleteServiceProvider":
            return DeleteSp()
         
    def patch(self, route):
        if route == "updateServiceProvider":
            return UpdateSp()
        