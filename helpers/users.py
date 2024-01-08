from flask import request
import uuid
from config.db import db

from model.quicktask import *



liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        u_username = (request.json.get('username'))
        u_email = (request.json.get('email'))
        u_password = (request.json.get('password'))
        u_mobile = (request.json.get('mobile'))
        u_address = (request.json.get('address'))
        u_country = (request.json.get('country'))
        u_city = (request.json.get('city'))
        
        new_user = User()
        new_user.u_username = u_username
        new_user.u_email = u_email
        new_user.u_password = u_password
        new_user.u_mobile = u_mobile
        new_user.u_address = u_address
        new_user.u_country = u_country
        new_user.u_city = u_city
        
        db.session.add(new_user)
        db.session.commit()

        nouvel_hotel =(reponse)
        liste_users.append(nouvel_hotel)

        reponse['u_username'] = u_username
        reponse['u_email'] = u_email
        reponse['u_password'] = u_password
        reponse['u_mobile'] = u_mobile
        reponse['u_address'] = u_address
        reponse['u_country'] = u_country
        reponse['u_city'] = u_city
        reponse['status'] = 'htl created from helper'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def ReadUser():
    reponse = {}

    try:
        readuser = User.query.filter_by(id = 1).first()
        db.session.add(readuser)
        db.session.commit()

        reponse['status'] = 'Succes'
        reponse = liste_users

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def UpdateUser  ():
    reponse = {}

    try:
        updateuser = User.query.filter_by(id = 8).first()
        db.session.add(updateuser)
        db.session.commit()


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


def LoginUser  ():
    reponse = {}

    try:
        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




        # readuser = User.query.all()
        # if readuser:
        #     for user in readuser:
        #         all_user = ""
        #             'username' : user.u_username,
        #             'email' : user.u_email,
        #             "password" = user.u_password,
        #             "mobile" = user.u_mobile,
        #             "address" = user.u_address,
        #             "country" = user.u_country,
        #             "city" = user.u_city
        #             }
