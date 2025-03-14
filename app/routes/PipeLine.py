from app.common.config import DOCS_SAVE_PATH
from fastapi import APIRouter
from docx import Document
from app.services.llm_models import get_whisper_model

from app.routes.VideoManager import download_video, rename_video, delete_video
from app.routes.FileManager import delete_file
from app.models import Video, Document_
from fastapi.responses import FileResponse
from fastapi import BackgroundTasks

router = APIRouter()

@router.post("/Speech-to-Text/", response_class=FileResponse)
async def Speech2Text(video: Video, backgroundtasks: BackgroundTasks):
    """
    `Pipeline API`
    :param VideoDownload:
    :return docs:
    """
    download_result = await download_video(video)
    video.path = download_result["video_path"]

    rename_result = await rename_video(video)
    video.path = rename_result["video_path"]
    video.title = rename_result["video_title"]

    whisperAI_model = get_whisper_model()
    result = whisperAI_model.transcribe(video.path, task="transcribe")

    document = Document_(path=f"{DOCS_SAVE_PATH}/{video.title}.docx")
    doc = Document()
    doc.add_paragraph(result['text'])
    doc.save(document.path)

    await delete_video(video)
    
    try:
        backgroundtasks.add_task(delete_file, document)
    except Exception as e:
        print(f"Error adding background task: {e}")

    return FileResponse(path=document.path, filename=f"{video.title}.docx")
