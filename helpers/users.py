from flask import request
import uuid
from config.db import db

from model.quicktask import User



liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        user_username = (request.json.get('username'))
        user_email = (request.json.get('email'))
        user_password = (request.json.get('password'))
        user_mobile = (request.json.get('mobile'))
        user_address = (request.json.get('address'))
        user_country = (request.json.get('country'))
        user_city = (request.json.get('city'))
        
        # new_user.user_username = user_username
        # new_user.user_email = user_email
        # new_user.user_password = user_password
        # new_user.user_mobile = user_mobile
        # new_user.user_address = user_address
        # new_user.user_country = user_country
        # new_user.user_city = user_city
        
        # db.session.add(new_user)
        # db.session.commit()

        nouvel_hotel =(reponse)
        liste_users.append(nouvel_hotel)

        reponse['user_username'] = user_username
        reponse['user_email'] = user_email
        reponse['user_password'] = user_password
        reponse['user_mobile'] = user_mobile
        reponse['user_address'] = user_address
        reponse['user_country'] = user_country
        reponse['user_city'] = user_city
        reponse['status'] = 'htl created from helper'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def ReadUser():
    response = {}

    try:


        readAllUser = User.query.all()

        if readAllUser:
            user_informations = []

            for user in readAllUser:
                user_infos = {
                    'username': user.u_username,

                    
                }


            user_informations.append(user_infos)

            response['status'] = 'success'
            response ['users'] = user_informations

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return reponse


def UpdateUser  ():
    reponse = {}

    try:
        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteUser  ():
    reponse = {}

    try:
        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse

