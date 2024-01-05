from flask_restful import Resource



class UsersApi(Resource):
    def post(self, route):
        if route == "CreateUser":
            return "True"
