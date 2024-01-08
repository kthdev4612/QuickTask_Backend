from flask import request
import uuid
from config.db import db

from model.quicktask import Services


   
def CreateService():
    reponse = {}

    try:
        s_servicename = (request.json.get('servicename'))
        s_description = (request.json.get('description'))
        s_price = (request.json.get('price'))

        new_service = Services()
        new_service.s_servicename = s_servicename
        new_service.s_description = s_description
        new_service.s_price = s_price
        
        db.session.add(new_service)
        db.session.commit()

        # nouveau_service =(reponse)
        # liste_users.append(nouveau_service)

        reponse['servicename'] = s_servicename
        reponse['description'] = s_description
        reponse['price'] = s_price
        reponse['status'] = 'htl created from helper'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse




def ReadAllService():
    response = {}

    try:
        readAllService = Services.query.all()

        if readAllService:
            service_informations = []

            for service in readAllService:
                service_infos = {
                    'servicename': service.s_servicename,
                    'description': service.s_description,
                    'price': service.s_price,            
                }

                service_informations.append(service_infos)

            response['status'] = 'success'
            response ['users'] = service_informations
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response

def ReadSingleService():
    response = {}

    try:
        readSingleService = Services.query.filter_by(id=2).first()

        if readSingleService:
            service_infos = {
                'servicename': readSingleService.s_servicename,
                'description': readSingleService.s_description,
                'price': readSingleService.s_price,
            }

            response['status'] = 'success'
            response['user'] = service_infos
        else:
            response['status'] = 'erreur'
            response['motif'] = 'aucun'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response



def UpdateService  ():
    reponse = {}

    try:
        updateservice = Services.query.filter_by(id = 2).first()

        if updateservice:
            updateservice.s_servicename = request.json.get('servicename', updateservice.s_servicename)
            updateservice.s_description = request.json.get('description', updateservice.s_description)
            updateservice.s_price = request.json.get('price', updateservice.s_price  )

            db.session.add(updateservice)
            db.session.commit()

            reponse['status'] = 'Succes'
        else:
            reponse['status'] = 'User not found'

    except Exception as e:
        reponse['error_description'] = str(e)
        reponse['status'] = 'error'

    return reponse


def DeleteService():
    response = {}

    try:
        deleteservice = Services.query.filter_by(id=1).first()

        if deleteservice:
            db.session.delete(deleteservice)
            db.session.commit()
            response['status'] = 'success'
        else:
            response['status'] = 'error'
            response['motif'] = 'utilisateur non trouvé'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response




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
