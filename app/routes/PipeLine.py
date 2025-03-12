<<<<<<< HEAD
from fastapi import APIRouter



router = APIRouter()
=======
from app.common.config import DOCS_SAVE_PATH
from fastapi import APIRouter
from docx import Document
from app.services.llm_models import get_whisper_model

from app.routes.VideoManager import download, rename, delete
from app.models import Video

router = APIRouter()

@router.put("/Speech-to-Text")
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

    return {f"[Speech-to-Text 완료] path : {video}"}
>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
