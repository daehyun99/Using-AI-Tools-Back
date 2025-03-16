from fastapi import APIRouter
from fastapi import FastAPI, File, UploadFile

import os
from app.services.translatemanage import translate_
from app.models import Document_, TranslateService

from fastapi.responses import FileResponse


router = APIRouter(prefix="/translate")


@router.put("/v1/", response_class=FileResponse)
async def translate(document: Document_, service: TranslateService):
    """
    `Translate API`
    :param file:
    :return:
    """
    try:
        new_document_title_ext, new_document_path = await translate_(document.path, service)
        return FileResponse(path=new_document_path, filename=f"{new_document_title_ext}")
    except Exception as e:
        print(f"오류 발생: {e}")  # 에러 메시지 출력
