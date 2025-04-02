from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile

import os
from app.services.translatemanage import translate_
from app.models import Document_, TranslateService

from app.database.conn import db

from fastapi.responses import FileResponse
from app.api import exceptions as ex
from app.common.utils import logging_response
from app.common.utils import generate_metadata

router = APIRouter(prefix="/translate")

layer = "PRESENTATION"

@router.put("/v1/", response_class=FileResponse)
async def translate(document: Document_, service: TranslateService):
    """
    `Translate API`
    :param file:
    :return:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        mono_document_title_ext, dual_document_title_ext, new_document_path = await translate_(document.path, service, session=session, correlation_id=correlation_id)
        return FileResponse(path=new_document_path, filename=f"{mono_document_title_ext}")
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)