from fastapi import APIRouter, Depends

from app.services.emailmanage import send_email_, send_email2_
from starlette.background import BackgroundTasks

from app.common.utils import logging_request, logging_response
from app.common.utils import generate_metadata

from app.api.request import SuccessRequest
from app.api.response import SuccessResponse

from app.api import exceptions as ex

from sqlalchemy.orm import Session
from app.database.conn import db

router = APIRouter(prefix="/email")

layer = "PRESENTATION"

@router.post("/send/")
async def send_email(file_path, receiver, session, correlation_id): # 번역본 전송 API
    """
    `Email API`
    :return:
    """
    try:
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)

        send_email_(file_path, receiver, session=session, correlation_id=correlation_id)
 
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)


@router.post("/send_id_pw/")
async def send_email_id_pw(id, pw, email, session, correlation_id): # id, pw 전송 API
    """
    `Email API`
    :return id, pw:
    """
    try:
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)

        await send_email2_(id, pw, email, session=session, correlation_id=correlation_id)
 
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
