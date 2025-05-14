from fastapi import APIRouter, Request, Depends
from app.models import Email, OneTimeAuth

import bcrypt
from app.routes.EmailManager import send_email_id_pw
from app.common.utils import generate_id, generate_pw, generate_metadata, is_valid_email

from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.crud import create_user 
from app.database.crud import read_user_by_email, read_user_by_uuid
from app.database.crud import update_user

from app.api.response import SuccessResponse
from app.api import exceptions as ex
from app.common.utils import logging_response

from app.common.config import test_receiver # 임시

layer = "PRESENTATION"

router = APIRouter(prefix="/Auth")

@router.post("/register/")
async def register(email: Email, session: Session = Depends(db.get_db)):
    """
    `Auth API`
    :param ID, PW, Email:
    :return :
    """
    try:
        correlation_id = generate_metadata()
        # logging_request

        if not is_valid_email(email.email):
            error_message = ex.ErrorResponse(ex="이메일 형식이 맞지 않습니다.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
        if read_user_by_email(session=session, email=email.email):
            error_message = ex.ErrorResponse(ex="이미 존재하는 이메일입니다.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
        
        id, pw = generate_id(), generate_pw()
        password_hash = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
        create_user(session=session, uuid=id, email=email.email, password_hash=password_hash, service_enabled=True)
        
        await send_email_id_pw(id, pw, email.email, session=session, correlation_id=correlation_id)

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
@router.post("/re-register/")
async def re_register(session: Session = Depends(db.get_db)):
    """
    `Auth API`

    :return:
    """
    try:
        correlation_id = generate_metadata()
        # logging_request

        email = test_receiver # 임시

        pw = generate_pw()
        password_hash = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
        user = update_user(session=session, email=email, password_hash=password_hash, service_enabled=True)

        await send_email_id_pw(user.uuid, pw, user.email, session=session, correlation_id=correlation_id)

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
@router.post("/one-time-auth/")
def one_time_auth(auth: OneTimeAuth, session: Session = Depends(db.get_db)):
    """
    `Auth API`

    :return:
    """
    try:
        correlation_id = generate_metadata()
        # logging_request

        user = read_user_by_uuid(session=session, uuid=auth.uuid)

        if user.uuid != auth.uuid or not bcrypt.checkpw(auth.password.encode("utf-8"), user.password_hash.encode("utf-8")) or not user.service_enabled == True:
            error_message = ex.ErrorResponse()
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
        
        success_message = SuccessResponse(data= {"email": user.email})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)