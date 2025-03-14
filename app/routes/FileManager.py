from fastapi import APIRouter
from fastapi import FastAPI, UploadFile

import os
from app.models import Document_
from app.services.filemanage import delete_file_, upload_file_

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
async def upload_file(file: UploadFile):
    """
    `File API`
    :param UploadFile:
    :return:
    """
    try:
        await upload_file_(file)
        print(f"🚩 문서 업로드 완료")
    except Exception as e:
        print(f"Error during upload: {e}") # TODO: logging 추가, Error handling 추가

    return {"message": "[문서 업로드 완료]"}