from fastapi import APIRouter
from fastapi import FastAPI, UploadFile

import os, aiofiles
from app.models import Document_
from app.services.filemanage import delete_file_
from app.common.config import DOCS_SAVE_PATH

from fastapi.responses import FileResponse

router = APIRouter(prefix="/file")

@router.post("/download/", response_class=FileResponse)
async def download_file(document: Document_):
    """
    `File API`
    :param docs_path:
    :return docs:
    """
    try:
        document_name = os.path.basename(document.path)
        return FileResponse(path=document.path, filename=f"{document_name}")
    except Exception as e:
        return {"error": f"Error during download_file: {e}"}

@router.delete("/delete/")
async def delete_file(document: Document_):
    """
    `File API`
    :param Document_:
    :return:
    """
    try:
        delete_file_(document.path)
        print(f"🚩 문서 삭제 완료 : {document.path}")
    except Exception as e:
        print(f"Error during delete: {e}")
    return {"message": f"[문서 삭제 완료]"}

@router.post("/upload/")
async def upload_file(file: UploadFile, DOCS_SAVE_PATH=DOCS_SAVE_PATH):
    """
    `File API`
    :param file:
    :return:
    """
    file_path = f"{DOCS_SAVE_PATH}/{file.filename}"

    async with aiofiles.open(file_path, 'wb') as out_file:
        content = await file.read()
        await out_file.write(content)

    return {"file_path": file_path, "message": "[파일 업로드 완료]"}