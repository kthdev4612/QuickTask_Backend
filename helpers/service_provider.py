from flask import request
import uuid
from config.db import db
from model.quicktask import Service_Provider



def CreateSp():

    response = {}

    try:
        detail = request.json.get('detail')
        uid = str(uuid.uuid4())



        new_sp = Service_Provider()
        new_sp.sp_service_details = detail
        new_sp.sp_uid = uid

        
        db.session.add(new_sp)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateSp():
    response = {}

    try:

        update_sp = Service_Provider.query.filter_by(sp_uid=2).first()
        
        detail = request.json.get('detail')

        if detail :
            update_sp.sp_service_details = detail

       
        db.session.add(update_sp)
        db.session.commit()

        response['status'] = 'success'
        response['message'] = "le service provider a été mises à jour avec succès!"


    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeleteSp():
    response = {}

    try:
        sp_id = request.json.get('sp_uid')

        deleted_sp = Service_Provider.query.filter_by(id=sp_id).first()

   
        db.session.delete(deleted_sp)
        db.session.commit()
        response['status'] = 'success'
        response['message'] = "le service provider a été supprimé avec succès!"
   
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def GetAllSp():
    response = {}
    
    try:
        all_sp = Service_Provider.query.all()

        sp_informations = []

        for sp in all_sp:
            sp_info = {
                'sp_uid': sp.sp_uid,
                'service provider detail': sp.sp_service_details,
                
            }
            sp_informations.append(sp_info)

        response['status'] = 'success'
        response ['users'] = sp_informations

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def GetSingleSp():
    response = {}

    try:
        sp_id = request.json.get('sp_uid')
        sp = Service_Provider.query.filter_by(id=sp_id).first()

        sp_info = {
            'sp_uid': sp.sp_uid,
            'service provider detail': sp.sp_service_details,

        }

        response['status'] = 'success'
        response['user'] = sp_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

