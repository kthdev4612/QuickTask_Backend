from flask import request
import uuid
from config.db import db
from model.quicktask import Payment



def CreatePayment():

    response = {}

    try:
        amount = request.json.get('amount')
        paymenDate = request.json.get('payment_date')
        uid = str(uuid.uuid4())



        new_payment = Payment()

        new_payment.p_amount = amount
        new_payment.p_paymentDate = paymenDate
        new_payment.p_uid = uid

        
        db.session.add(new_payment)
        db.session.commit()

        response['satus'] = 'success'

    except Exception as e:
        response['error_description'] = str(e)
        response['status'] = 'error'

    return response


def UpdatePayment():
    response = {}

    try:

        update_payment = Payment.query.filter_by(p_uid=2).first()
        
        amount = request.json.get('amount')
        paymenDate = request.json.get('payment_date')

        if amount and paymenDate:
            update_payment.p_amount = amount
            update_payment.p_paymentDate = paymenDate

       
        db.session.add(update_payment)
        db.session.commit()

        response['status'] = 'success'
        response['message'] = "la payment a été mises à jour avec succès!"



    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def DeletePayment():
    response = {}

    try:
        payment_id = request.json.get('p_uid')

        deleted_payment = Payment.query.filter_by(id=payment_id).first()
   
        db.session.delete(deleted_payment)
        db.session.commit()
        response['status'] = 'success'
        response['message'] = f"le payment a été supprimé avec succès!"
   
    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response


def GetAllPayment():
    response = {}
    
    try:
        all_payment = Payment.query.all()

        Payment_informations = []

        for payment in all_payment:
            payment_info = {
                'p_uid': payment.p_uid,
                'amount': payment.p_amount,
                'payment date': payment.p_paymentDate,
                
            }
            Payment_informations.append(payment_info)

        response['status'] = 'success'
        response ['users'] = Payment_informations

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response




def GetSinglePayment():
    response = {}

    try:
        payment_id = request.json.get('p_uid')

        payment = Payment.query.filter_by(u_uid=payment_id).first()

        payment_info = {
            'p_uid': payment.p_uid,
            'amount': payment.p_amount,
            'payment date': payment.p_paymentDate,
        }

        response['status'] = 'success'
        response['user'] = payment_info

    except Exception as e:
        response['status'] = 'error'
        response['error_description'] = str(e)

    return response

