from app.common.config import DOCS_SAVE_PATH
from fastapi import APIRouter
from docx import Document
from app.services.llm_models import get_whisper_model

from app.routes.VideoManager import download, rename, delete
from app.routes.FileManager import download_file
from app.models import Video, Document_
from fastapi.responses import FileResponse

router = APIRouter()

@router.post("/Speech-to-Text/", response_class=FileResponse)
async def Speech2Text(video: Video):
    """
    `Pipeline API`
    :param VideoDownload:
    :return docs:
    """
    download_result = await download(video)
    video.path = download_result["video_path"]

    rename_result = await rename(video)
    video.path = rename_result["video_path"]
    video.title = rename_result["video_title"]

    whisperAI_model = get_whisper_model()
    result = whisperAI_model.transcribe(video.path, task="transcribe")

    doc = Document()
    doc.add_paragraph(result['text'])
    doc.save(f"{DOCS_SAVE_PATH}/{video.title}.docx")

    await delete(video)

    document = Document_
    document.path = f"{DOCS_SAVE_PATH}/{video.title}.docx"
    await download_file(document)

    return FileResponse(path=document.path, filename=f"{video.title}.docx")
