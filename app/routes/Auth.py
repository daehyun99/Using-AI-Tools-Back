from fastapi import APIRouter, Request, Depends, BackgroundTasks
from app.models import Email, OneTimeAuth

import bcrypt
from app.routes.EmailManager import send_email_id_pw
from app.common.utils import generate_id, generate_pw, generate_metadata, is_valid_email

from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.crud import create_user 
from app.database.crud import read_user_by_email, read_user_by_uuid
from app.database.crud import update_user

from app.api.request import SuccessRequest
from app.api.response import SuccessResponse, FailResponse

from app.api import exceptions as ex

from app.common.utils import logging_request, logging_response

from app.common.config import test_receiver # 임시

layer = "PRESENTATION"

router = APIRouter(prefix="/Auth")

@router.post("/register/")
async def register(email: Email, backgroundtasks: BackgroundTasks, session: Session = Depends(db.get_db)):
    """
    `Auth API`
    :param ID, PW, Email:
    :return :
    """
    try:
        correlation_id = generate_metadata()
        message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=message)

        if not is_valid_email(email.email):
            message = FailResponse(msg="❎ 이메일 형식이 맞지 않습니다.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
        if read_user_by_email(session=session, email=email.email):
            message = FailResponse(msg="❎ 이미 존재하는 이메일입니다.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
        
        id, pw = generate_id(), generate_pw()
        password_hash = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
        create_user(session=session, uuid=id, email=email.email, password_hash=password_hash, service_enabled=True)
        
        backgroundtasks.add_task(send_email_id_pw, id, pw, email.email, session=session, correlation_id=correlation_id)

        message = SuccessResponse(msg="✅ ID와 PW가 발급되었습니다. 이메일을 확인해주세요.")
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
    except Exception as e:
        message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
    
@router.post("/re-register/")
async def re_register(backgroundtasks: BackgroundTasks, session: Session = Depends(db.get_db)):
    """
    `Auth API`

    :return:
    """
    try:
        correlation_id = generate_metadata()
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)

        email = test_receiver # 임시

        pw = generate_pw()
        password_hash = bcrypt.hashpw(pw.encode("utf-8"), bcrypt.gensalt())
        user = update_user(session=session, email=email, password_hash=password_hash, service_enabled=True)

        backgroundtasks.add_task(send_email_id_pw, user.uuid, pw, user.email, session=session, correlation_id=correlation_id)

        success_message = SuccessResponse(msg="✅ ID와 PW가 재발급되었습니다. 이메일을 확인해주세요.")
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
        message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=message)

        user = read_user_by_uuid(session=session, uuid=auth.uuid)

        if user.uuid != auth.uuid or not bcrypt.checkpw(auth.password.encode("utf-8"), user.password_hash.encode("utf-8")):
            message = FailResponse(msg="❎ ID 또는 PW를 확인해주세요.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
        
        if not user.service_enabled == True:
            message = FailResponse(msg="❎ 번역 가능횟수가 없습니다.")
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
        
        message = SuccessResponse(data= {"email": user.email})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)
    except Exception as e:
        message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=message)