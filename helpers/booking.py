from flask import request
import uuid
from config.db import db
from model.quicktask import Booking



def CreateBooking():

    response = {}

    try:
        status = request.json.get('status')
        new_booking = Booking()
        new_booking.b_status = status

        
        db.session.add(new_booking)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdateBooking():
    response = {}

    try:

        update_booking = Booking.query.filter_by(id=2).first()
        
        status = request.json.get('status')
        if status:
            update_booking.b_status = status
        
        else:
            response["status"] : 'error'
        

        db.session.add(update_booking)
        db.session.commit()
        response['status'] = 'success'
        response['message'] = "la commande a été mises à jour avec succès!"



    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeleteBooking():
    response = {}

    try:
        deleted_user = Booking.query.filter_by(id=1).first()

   
        db.session.delete(deleted_user)
        db.session.commit()
        response['status'] = 'success'
        response['message'] = f"la commande a été supprimé avec succès!"
   
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response



def GetAllBooking():
    response = {}
    
    try:
        all_booking = Booking.query.all()

        booking_informations = []

        for booking in all_booking:
            booking_info = {
                'booking_satuts': booking.b_status
                
            }
            booking_informations.append(booking_info)

        response['status'] = 'success'
        response ['users'] = booking_informations

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def GetSingleBooking():
    response = {}

    try:
        booking = Booking.query.filter_by(id=3).first()

        booking_info = {
            'booking_satuts': booking.b_status
        }

        response['status'] = 'success'
        response['user'] = booking_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

