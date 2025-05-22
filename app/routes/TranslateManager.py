from app.common.const import DOCS_SAVE_PATH
from fastapi import APIRouter, Request, Depends
from app.common.utils import generate_metadata

from app.routes.FileManager import delete_file, upload_file
from app.routes.EmailManager import send_email
from app.services.translatemanage import translate_

import os
from app.models import Document_, TranslateService
from fastapi import UploadFile, BackgroundTasks

from app.api.request import SuccessRequest
from app.api.response import SuccessResponse, FailResponse
from app.api import exceptions as ex
from app.common.utils import logging_request, logging_response

from sqlalchemy.orm import Session
from app.database.conn import db
from app.database.crud import read_user_by_email, create_service_usage
from app.database.crud import update_user

layer = "PRESENTATION"

router = APIRouter()

@router.post("/Translate/")
async def Translate(file: UploadFile, service: TranslateService, email_address: str, backgroundtasks: BackgroundTasks, session: Session = Depends(db.get_db)):
    """
    `Pipeline API`
    :param file:
    :return docs:
    """
    try:
        correlation_id = generate_metadata()
        success_message = SuccessRequest(data={"file": file.filename, "service": service, "email_address": email_address})
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
        
        result = await upload_file(file, session=session, correlation_id=correlation_id)
        document = Document_(path=result.data["path"])

        user = read_user_by_email(session=session, email=email_address)
        create_service_usage(session=session, uuid=user.uuid, correlation_id=correlation_id)

        base_name = os.path.basename(document.path)
        document_title, document_ext = os.path.splitext(base_name)
        mono_document_title_ext = f"{document_title}" + "-mono" + f"{document_ext}"
        dual_document_title_ext = f"{document_title}" + "-dual" + f"{document_ext}"

        document.mono_path = os.path.join(f"{DOCS_SAVE_PATH}", mono_document_title_ext)
        document.dual_path = os.path.join(f"{DOCS_SAVE_PATH}", dual_document_title_ext)

        backgroundtasks.add_task(translate_, document.path, service, session=session, correlation_id=correlation_id)
        backgroundtasks.add_task(send_email, file_path=document.mono_path, receiver=email_address,session=session, correlation_id=correlation_id)
        backgroundtasks.add_task(update_user, session=session, email=user.email, password_hash=user.password_hash, service_enabled=False)
        backgroundtasks.add_task(delete_file, document, session=session, correlation_id=correlation_id)        

        success_message = SuccessResponse(msg="파일 번역 중입니다. 번역 완료 후, 이메일로 전송드리겠습니다.")
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)