from flask import request
import uuid
from config.db import db

from model.quicktask import *



liste_users = []
   
def CreateUser():
    reponse = {}

    try:
        user_ref = int(uuid.uuid4())
        user_username = (request.json.get('username'))
        user_email = (request.json.get('email'))
        user_password = (request.json.get('password'))
        user_mobile = (request.json.get('mobile'))
        user_address = (request.json.get('address'))
        user_country = (request.json.get('country'))
        user_city = (request.json.get('city'))
        
        # new_user = User()
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

        reponse['user_ref'] = user_ref
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
    reponse = {}

    try:
        user_ref = (request.json.get('ref'))
        read_user = User.query.filter_by(user_ref = user_ref).first()

        reponse['User'] = read_user
        reponse['status'] = 'Succes'


    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




# def UpdateUser():
#     reponse = {}
    
    
#     try:
#         # ref = (request.json.get('htl_ref'))
#         update_user = User.query.filter_by(htl_name = "Foley").first()

#         if update_user:

#             us_username = (request.json.get('username'))
#             us_email = (request.json.get('email'))
#             us_password = (request.json.get('password'))
#             us_details = (request.json.get('details'))
            
#             #update_hotel.htl_name = htl_name
#             # update_user.htl_location = htl_location
#             # update_user.htl_description = htl_description
#             # update_user.htl_phone_tel = htl_phone_tel
#             # update_user.htl_star = htl_star
            
#             db.session.add(update_user)
#             db.session.commit()

#             # nouvel_hotel =(reponse)
#             # liste_hotels.append(nouvel_hotel)

#             reponse['us_username'] = us_username
#             reponse['us_email'] = us_email
#             reponse['us_password'] = us_password
#             reponse['us_details'] = us_details
#             reponse['status'] = 'This information has been successfully updated'

#             return reponse

#         else:
#             reponse['error_description'] = str(e)
#             reponse['status'] = 'error'

#         return reponse

#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'





# def deleteHotel():
#     reponse = {}
#     try:
#         ref = (request.json.get('htl_ref'))
#         delete_Hotel = Hotel.query.filter_by(htl_ref = ref).first()


#         db.session.delete(delete_Hotel)
#         db.session.commit()

#         reponse['status'] = 'This hotel with this reference has been successfully deleted'


#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse





# def raedHotel():
#     return liste_hotels


# def updateHotel():
#     reponse = {}
    
    
#     try:

#         update_hotel = Hotel.query.filter_by(htl_id = 2).first()

#         if update_hotel:

#             htl_name = (request.json.get('name'))
#             htl_location = (request.json.get('location'))
#             htl_description = (request.json.get('description'))
#             htl_phone_tel = (request.json.get('phone'))
#             htl_star = (request.json.get('star'))
            
#             #update_hotel.htl_name = htl_name
#             update_hotel.htl_location = htl_location
#             update_hotel.htl_description = htl_description
#             update_hotel.htl_phone_tel = htl_phone_tel
#             update_hotel.htl_star = htl_star
            
#             db.session.add(update_hotel)
#             db.session.commit()

#             nouvel_hotel =(reponse)
#             liste_hotels.append(nouvel_hotel)

#             reponse['htl_name'] = htl_name
#             reponse['htl_location'] = htl_location
#             reponse['htl_description'] = htl_description
#             reponse['htl_phone_tel'] = htl_phone_tel
#             reponse['htl_star'] = htl_star
#             reponse['status'] = 'This information has been successfully updated'

#             return reponse

#         else:
#             reponse['error_description'] = str(e)
#             reponse['status'] = 'error'



#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'


# def deleteHotel():
#     reponse = {}
#     try:
#         ref = (request.json.get('htl_ref'))
#         delete_Hotel = Hotel.query.filter_by(htl_ref = ref).first()


#         db.session.delete(delete_Hotel)
#         db.session.commit()

#         reponse['status'] = 'This hotel with this reference has been successfully deleted'


#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse



# def addition():
#     reponse = {}
#     try:
#         a = float(request.json.get('premier_nombre'))
#         b = float(request.json.get('deuxieme_nombre'))
#         result = a + b
#         reponse['resultat'] = result
#         reponse['status'] = 'succes'
#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse

# def soustraction():
#     reponse = {}
#     try:
#         a = float(request.json.get('premier_nombre'))
#         b = float(request.json.get('deuxieme_nombre'))
#         result = a - b
#         reponse['resultat'] = result
#         reponse['status'] = 'succes'
#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'


#     return reponse


# def multiplication():
#     reponse = {}
#     try:
#         a = float(request.json.get('premier_nombre'))
#         b = float(request.json.get('deuxieme_nombre'))
#         result = a * b
#         reponse['resultat'] = result
#         reponse['status'] = 'succes'
#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse


# def division():
#     reponse = {}
#     try:
#         a = float(request.json.get('premier_nombre'))
#         b = float(request.json.get('deuxieme_nombre'))
#         result = a / b
#         reponse['resultat'] = result
#         reponse['status'] = 'succes'
#     except Exception as e:
#         reponse['error_description'] = str(e)
#         reponse['status'] = 'error'

#     return reponse