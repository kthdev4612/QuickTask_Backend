from flask import request
import uuid
from config.db import db

from model.quicktask import User



liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        username = (request.json.get('username'))
        email = (request.json.get('email'))
        password = (request.json.get('password'))
        mobile = (request.json.get('mobile'))
        address = (request.json.get('address'))
        country = (request.json.get('country'))
        city = (request.json.get('city'))
        
        new_user = User()
        new_user.u_username = username
        new_user.u_email = email
        new_user.u_password = password
        new_user.u_mobile = mobile
        new_user.u_address = address
        new_user.u_country = country
        new_user.u_city = city
        
        db.session.add(new_user)
        db.session.commit()

        nouvel_hotel =(reponse)
        liste_users.append(nouvel_hotel)

        reponse['username'] =username
        reponse['email'] =email
        reponse['password'] =password
        reponse['mobile'] =mobile
        reponse['address'] =address
        reponse['country'] =country
        reponse['city'] =city
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
                    'email': user.u_email,

                    
                }


            user_informations.append(user_infos)

            response['status'] = 'success'
            response ['users'] = user_informations
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun'

 

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateUser  ():
    reponse = {}

    try:
        updateuser = User.query.filter_by(id = 2).first()

        if updateuser:
            updateuser.username = request.json.get('username',updateuser.email)
            updateuser.email = request.json.get('email', updateuser.email)
            updateuser.password = request.json.get('password', updateuser.password)
            updateuser.mobile = request.json.get('mobile', updateuser.mobile)
            updateuser.address = request.json.get('address', updateuser.address)
            updateuser.country = request.json.get('country', updateuser.country)
            updateuser.city = request.json.get('city', updateuser.city)

            db.session.commit()

            reponse['status'] = 'Succes'
        else:
            reponse['status'] = 'User not found'

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
