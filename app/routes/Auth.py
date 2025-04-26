from fastapi import APIRouter, Request, Depends
from app.models import Email

from app.routes.EmailManager import send_email_id_pw
from app.common.utils import generate_id_pw, generate_metadata, is_valid_email

from sqlalchemy.orm import Session
from app.database.conn import db

from app.api import exceptions as ex
from app.common.utils import logging_response

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

        # 1. 이메일에 대한 검증 
            # ✅ 형식 확인
        if not is_valid_email(email.email):
            error_message = ex.ErrorResponse(ex=e)
            return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
        
        # 2. 이메일에 대한 고유 ID와 PW를 발급 및 DB로 저장
            # 중복 확인
            # ✅ 발급
            # DB 저장
        id, pw = generate_id_pw()
        
        # 3. 해당 이메일로 고유 ID와 PW를 전송
        await send_email_id_pw(id, pw, email.email, session=session, correlation_id=correlation_id)
        print("id, pw", id, pw)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)