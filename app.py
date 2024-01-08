from flask import Flask, render_template
import os
from flask_restful import Resource, Api
from config.db import db
from config.constant import *
from model.quicktask import *
from resources.users import UsersApi
from resources.booking import BookingApi
from resources.payment import PaymentApi
from resources.service_provider import Service_ProviderApi
from resources.services import ServicesApi
from flask_migrate import Migrate


app = Flask(__name__)



app.secret_key = os.urandom(24)
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = LIEN_BASE_DE_DONNEES
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False


db.init_app(app)

migrate = Migrate(app, db)
api = Api(app)





@app.route('/a')    
def home():
    print('HELLO IM HERE')
    return render_template('index.html')

api.add_resource(UsersApi, '/api/user/<string:route>', endpoint='all_user', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(BookingApi, '/api/booking/<string:route>', endpoint='all_booking', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(PaymentApi, '/api/payment/<string:route>', endpoint='all_payment', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(Service_ProviderApi, '/api/service_provider/<string:route>', endpoint='all_service_provider', methods=['GET', 'POST', 'DELETE', 'PATCH'])
api.add_resource(ServicesApi, '/api/service/<string:route>', endpoint='all_services', methods=['GET', 'POST', 'DELETE', 'PATCH'])

if __name__ == '__main__':
    app.run(debug=True,  host="0.0.0.0")