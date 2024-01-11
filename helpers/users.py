from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask import request, jsonify
import uuid
from config.db import db
from model.quicktask import User
import bcrypt 
from werkzeug.security import check_password_hash


# liste_users = []
   
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
        u_uid = str(uuid.uuid4())

        hashed_password = bcrypt.hashpw(u_password.encode('utf-8'), bcrypt.gensalt())
        
        new_user = User()
        new_user.u_username = u_username
        new_user.u_email = u_email
        new_user.u_password = hashed_password
        new_user.u_mobile = u_mobile
        new_user.u_address = u_address
        new_user.u_country = u_country
        new_user.u_city = u_city
        new_user.u_uid = u_uid
        
        db.session.add(new_user)
        db.session.commit()

        # nouvel_hotel =(reponse)
        # liste_users.append(nouvel_hotel)

        # reponse['u_uid'] = u_uid
        # reponse['username'] = u_username
        # reponse['email'] = u_email
        # # reponse['password'] = u_password
        # reponse['mobile'] = u_mobile
        # reponse['address'] = u_address
        # reponse['country'] = u_country
        # reponse['city'] = u_city
        reponse['status'] = 'Succes'

    # except Exception as e:
    #     reponse['error_description'] = str(e)
    #     reponse['status'] = 'error'
    except:
        reponse['error'] = 'Incorrect data, recheck it'

    return reponse




def ReadAllUser():
    response = {}

    try:
        readAllUser = User.query.all()

        if readAllUser:
            user_informations = []

            for user in readAllUser:
                user_infos = {
                    'u_uid': user.u_uid,
                    'username': user.u_username,
                    'email': user.u_email,
                    # 'password': user.u_password,
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
        uid = request.json.get('u_uid')

        readSingleUser = User.query.filter_by(u_uid = uid).first()

        if readSingleUser:
            user_infos = {
                'u_uid': readSingleUser.u_uid,
                'username': readSingleUser.u_username,
                'email': readSingleUser.u_email,
                # 'password': readSingleUser.u_password,
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
        updateuser = User.query.filter_by(u_uid = "b7f45e6f-aecd-4a61-9122-639b71839d74").first()

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
        uid = request.json.get('u_uid')

        deleteuser = User.query.filter_by(u_uid=uid).first()

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
    response = {}
    responses = {}

    try:
        username = request.json.get('username')
        password = request.json.get('password')

        login_user = User.query.filter_by(u_username=username).first()

        if login_user and bcrypt.checkpw(password.encode('utf-8'), login_user.u_password.encode('utf-8')):
            access_token = create_access_token(identity=username)

            response = access_token


            responses['status'] = 'success'
            # response['message'] = 'Login successful'

        else:
            response['status'] = 'error'
            response['message'] = 'Invalid username or password'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response, responses


# def LoginUser():
#     response = {}

#     try:
#         username = (request.json.get('username'))
#         password = (request.json.get('password'))

#         login = User()

#         if login:
#             hash_password = password.encode('utf-8')

#             if bcrypt.checkpw(hash_password, login.u_password.encode('utf-8')) and username == login.u_username:
#                 # access_token = create_access_token(identity=username)

#                 # return jsonify(access_token=access_token), 200


#                 response['status'] = 'success'
#                 response['message'] = 'Login successful'
#             else:   
#                 # return jsonify({"msg": "Invalid credentials"}), 401

#                 response['status'] = 'error'
#                 response['message'] = 'Invalid username or password'

#     except Exception as e:
#         response['error_description'] = str(e)
#         response['status'] = 'error'

#     return response