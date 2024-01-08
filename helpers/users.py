from flask import request
import uuid
from config.db import db
from model.quicktask import User




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

        reponse['username'] = u_username
        reponse['email'] = u_email
        reponse['password'] = u_password
        reponse['mobile'] = u_mobile
        reponse['address'] = u_address
        reponse['country'] = u_country
        reponse['city'] = u_city
        reponse['status'] = 'htl created from helper'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def ReadAllUser():
    response = {}

    try:
        readAllUser = User.query.all()

        if readAllUser:
            user_informations = []

            for user in readAllUser:
                user_infos = {
                    'username': user.u_username,
                    'email': user.u_email,
                    'password': user.u_password,
                    'mobile': user.u_mobile,
                    'address': user.u_address,
                    'country': user.u_country,
                    'city': user.u_city,

                    
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

def ReadSingleUser():
    response = {}

    try:
        readSingleUser = User.query.filter_by(id=2).first()

        if readSingleUser:
            user_infos = {
                'username': readSingleUser.u_username,
                'email': readSingleUser.u_email,
                'password': readSingleUser.u_password,
                'mobile': readSingleUser.u_mobile,
                'address': readSingleUser.u_address,
                'country': readSingleUser.u_country,
                'city': readSingleUser.u_city,
            }

            response['status'] = 'success'
            response['user'] = user_infos
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
            updateuser.u_username = request.json.get('username', updateuser.u_username)
            updateuser.u_email = request.json.get('email', updateuser.u_email)
            updateuser.u_password = request.json.get('password', updateuser.u_password)
            updateuser.u_mobile = request.json.get('mobile', updateuser.u_mobile)
            updateuser.u_address = request.json.get('address', updateuser.u_address)
            updateuser.u_country = request.json.get('country', updateuser.u_country)
            updateuser.u_city = request.json.get('city', updateuser.u_city)

            db.session.add(updateuser)
            db.session.commit()

            reponse['status'] = 'Succes'
        else:
            reponse['status'] = 'User not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteUser():
    response = {}

    try:
        deleteuser = User.query.filter_by(id=2).first()

        if deleteuser:
            db.session.delete(deleteuser)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def LoginUser():
    reponse = {}

    username = (request.json.get('username'))
    password = (request.json.get('password'))

    login = User()

    if username == login.u_username:
        if password == login.u_password:
            reponse['status'] = "success"

    try:
        reponse['status'] = 'Succes'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse