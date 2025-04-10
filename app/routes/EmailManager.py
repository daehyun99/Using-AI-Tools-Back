from fastapi import APIRouter, Depends

from app.services.emailmanage import send_email_
from starlette.background import BackgroundTasks

from app.common.utils import logging_response
from app.common.utils import generate_metadata

from app.api.response import SuccessResponse
from app.api import exceptions as ex

from sqlalchemy.orm import Session
from app.database.conn import db

router = APIRouter(prefix="/email")

layer = "PRESENTATION"

@router.post("/send/")
async def send_email(file_path, receiver, session, correlation_id):
    """
    `Email API`
    :return:
    """
    try:
        # logging_request

        send_email_(file_path, receiver, session=session, correlation_id=correlation_id)
 
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    