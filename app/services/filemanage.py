import os
import aiofiles
from pathlib import Path

from app.common.config import base_dir
from app.common.const import DOCS_SAVE_PATH

from app.api.request import SuccessRequest
from app.api.response import SuccessResponse, FailResponse

from app.api import exceptions as ex

from app.common.utils import logging_request, logging_response

layer = "BUSINESS"

def delete_file_(file_path, session, correlation_id):
    try:
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)

        os.remove(f'{file_path}')
        
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    

async def upload_file_(file, session, correlation_id, DOCS_SAVE_PATH=DOCS_SAVE_PATH):
    try:
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)

        Path(DOCS_SAVE_PATH).mkdir(parents=True, exist_ok=True)
        
        file_path = f"{DOCS_SAVE_PATH}/{file.filename}"
        async with aiofiles.open(file_path, 'wb') as out_file:
            content = await file.read()
            await out_file.write(content)
        success_message = SuccessResponse(data={"path": file_path})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)


async def rename_file_(session, correlation_id):
    try:
        success_message = SuccessRequest()
        logging_request(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
        
        ...
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    