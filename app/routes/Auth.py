from fastapi import APIRouter, Request, Depends
from app.models import Email

from app.routes.EmailManager import send_email_id_pw
from app.common.utils import generate_id, generate_pw, generate_metadata, is_valid_email

from sqlalchemy.orm import Session
from app.database.conn import db

from app.api.response import SuccessResponse
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
        id, pw = generate_id(), generate_pw()
        
        # 3. 해당 이메일로 고유 ID와 PW를 전송
        await send_email_id_pw(id, pw, email.email, session=session, correlation_id=correlation_id)

        # 4. 테스트 코드 작성

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

        # 1. 검증
            # 설문시트에서 고유 ID에 관한 정보 불러오기
            # 새로운 PW 발급 대상임을 검증 (설문 참여를 했는지)
            # 입력된 고유 ID에 관한, 이메일 주소 불러오기

        # 2. 이메일에 대한 새로운 PW를 발급 및 DB 최신화
        pw = generate_pw()

        # 3. 해당 이메일로 갱신된 고유 ID와 PW를 전송
        await send_email_id_pw(id, pw, email.email, session=session, correlation_id=correlation_id)

        # 4. 테스트 코드 작성


        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)