from app.common.const import DOCS_SAVE_PATH
from fastapi import APIRouter, Request, Depends
from app.common.utils import generate_metadata

from app.routes.FileManager import delete_file, upload_file
from app.routes.EmailManager import send_email
from app.services.translatemanage import translate_

import os
from app.models import Document_, TranslateService
from fastapi import UploadFile, BackgroundTasks

from app.api.response import SuccessResponse
from app.api import exceptions as ex
from app.common.utils import logging_response

from sqlalchemy.orm import Session
from app.database.conn import db

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
        # logging_request
        
        result = await upload_file(file, session=session, correlation_id=correlation_id)
        document = Document_(path=result.data["path"])

        mono_document_title_ext, dual_document_title_ext, new_document_path = await translate_(document.path, service, session=session, correlation_id=correlation_id)

        document.mono_path = os.path.join(f"{DOCS_SAVE_PATH}", mono_document_title_ext)
        document.dual_path = os.path.join(f"{DOCS_SAVE_PATH}", dual_document_title_ext)
        
        backgroundtasks.add_task(send_email, file_path=document.mono_path, receiver=email_address,session=session, correlation_id=correlation_id)
        backgroundtasks.add_task(delete_file, document, session=session, correlation_id=correlation_id)

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)