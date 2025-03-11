from fastapi import APIRouter

from app.models import VideoRename, VideoDownload, VideoDelete
from app.services.videomanage import download_video, delete_video, rename_video
from app.common.config import VIDEO_SAVE_PATH, DOCS_SAVE_PATH

from app.errors.exceptions import APIException, FailDownloadVideo

from app.services.llm_models import whisperAI_model

router = APIRouter(prefix="/video")


@router.put("/download/")
async def download(video: VideoDownload):
    """
    `Video API`
    :param VideoDownload:
    :return video_path:
    """
    try:
        video_path = download_video(video.url)
        
    except Exception as e:
        raise FailDownloadVideo(ex=e)
    return f"[영상 다운로드 완료] path : {video_path}"

@router.get("/rename")
def rename(video: VideoRename):
    """
    `Video API`
    :param VideoRename:
    :return:
    """
    rename_video(video.path)

@router.delete("/delete/")
async def delete(video: VideoDelete):
    """
    `Video API`
    :param VideoDelete:
    :return:
    """
    try:
        delete_video(video.path)
        print(f"🚩 영상 삭제 완료 : {video.path}")
    except Exception as e:
        print(f"Error during delete: {e}") # Log the exception