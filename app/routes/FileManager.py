from fastapi import APIRouter
from fastapi import FastAPI, UploadFile

import os
from app.models import Document_
from app.services.filemanage import delete_file_, upload_file_, rename_file_

from app.database.conn import db

from fastapi.responses import FileResponse
from app.api.response import SuccessResponse
from app.common.utils import logging_response
from app.common.utils import generate_metadata

from app.api import exceptions as ex


router = APIRouter(prefix="/file")

layer = "PRESENTATION"

@router.post("/download/", response_class=FileResponse)
async def download_file(document: Document_):
    """
    `File API`
    :param docs_path:
    :return docs:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        document_name = os.path.basename(document.path)
        return FileResponse(path=document.path, filename=f"{document_name}")
    except Exception as e:
        error_message = ex.ErrorResponse_File(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)

@router.delete("/delete/")
async def delete_file(document: Document_):
    """
    `File API`
    :param Document_:
    :return:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        delete_file_(document.path, session=session, correlation_id=correlation_id)
        if (document.mono_path is not None) and (document.dual_path is not None):
            delete_file_(document.mono_path)
            delete_file_(document.dual_path)
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse_File(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    

@router.post("/upload/")
async def upload_file(file: UploadFile):
    """
    `File API`
    :param UploadFile:
    :return:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        file_path = await upload_file_(file, session=session, correlation_id=correlation_id)
        success_message = SuccessResponse(data={"file_path": file_path.data})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse_File(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)


@router.get("/rename/")
async def rename_file(document: Document_):
    """
    `File API`
    :param Document_:
    :return:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        rename_file_(session=session, correlation_id=correlation_id)
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        ...
        error_message = ex.ErrorResponse_File(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)