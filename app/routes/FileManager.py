import os
from fastapi import APIRouter

from app.models import Document
from fastapi.responses import FileResponse

router = APIRouter(prefix="/file")


@router.post("/download/", response_class=FileResponse)
async def download_file(document: Document):
    """
    `File API`
    :param docs_path:
    :return docs:
    """
    document_name = os.path.basename(document.path)
    return FileResponse(path=document.path, filename=f"{document_name}")