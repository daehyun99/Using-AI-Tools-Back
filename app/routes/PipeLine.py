from app.common.const import DOCS_SAVE_PATH
from fastapi import APIRouter, Request
from docx import Document
# from app.services.llm_models import get_whisper_model
# from app.common.lifespan import whisperAI_model
from app.common.utils import generate_metadata

from app.routes.VideoManager import download_video, rename_video, delete_video
from app.routes.FileManager import delete_file, upload_file
from app.routes.TranslateManager import translate
from app.services.translatemanage import translate_

import os
from app.models import Video, Document_, TranslateService
from fastapi.responses import FileResponse
from fastapi import UploadFile, BackgroundTasks

from app.api import exceptions as ex
from app.common.utils import logging_response

from app.database.conn import db

layer = "PRESENTATION"

router = APIRouter()

@router.post("/Speech-to-Text/")
async def Speech2Text(request: Request, video: Video, backgroundtasks: BackgroundTasks):
    """
    `Pipeline API`
    :param VideoDownload:
    :return docs:
    """
    session = next(db.session())
    correlation_id = generate_metadata()
    # logging_request
    

    download_result = await download_video(video, session=session, correlation_id=correlation_id)
    if download_result.status != 200 or not download_result.data:
        error_message = ex.ErrorResponse_Video()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
    video.path = download_result.data["video_path"]

    rename_result = await rename_video(video, session=session, correlation_id=correlation_id)
    if rename_result.status != 200 or not rename_result.data:
        error_message = ex.ErrorResponse_Video()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
    video.path = rename_result.data["video_path"]
    video.title = rename_result.data["video_title"]
    
    model = request.app.state.whisperAI_model
    
    # whisperAI_model = get_whisper_model(whisperAI_model= whisperAI_model, session=session, correlation_id=correlation_id)
    result = model.transcribe(video.path, task="transcribe")

    document = Document_(path=f"{DOCS_SAVE_PATH}/{video.title}.docx")
    doc = Document()
    doc.add_paragraph(result['text'])
    doc.save(document.path)

    await delete_video(video, session=session, correlation_id=correlation_id)
    
    try:
        backgroundtasks.add_task(delete_file, document, session=session, correlation_id=correlation_id)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)

    return FileResponse(path=document.path, filename=f"{video.title}.docx")

@router.post("/Translate/", response_class=FileResponse)
async def Translate(file: UploadFile, service: TranslateService, backgroundtasks: BackgroundTasks):
    """
    `Pipeline API`
    :param file:
    :return docs:
    """
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        
        result = await upload_file(file, session=session, correlation_id=correlation_id)
        document = Document_(path=result.data["path"])

        mono_document_title_ext, dual_document_title_ext, new_document_path = await translate_(document.path, service, session=session, correlation_id=correlation_id)

        document.mono_path = os.path.join(f"{DOCS_SAVE_PATH}", mono_document_title_ext)
        document.dual_path = os.path.join(f"{DOCS_SAVE_PATH}", dual_document_title_ext)
        

        backgroundtasks.add_task(delete_file, document, session=session, correlation_id=correlation_id)

        return FileResponse(path=new_document_path, filename=f"{mono_document_title_ext}")
    except Exception as e:
        print(f"Error during translate: {e}")