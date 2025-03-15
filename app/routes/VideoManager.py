from fastapi import APIRouter

from app.models import Video
from app.services.videomanage import download_video_, delete_video_, rename_video_
from app.common.config import VIDEO_SAVE_PATH, DOCS_SAVE_PATH

from app.errors.exceptions import APIException, FailDownloadVideo

from app.services.llm_models import whisperAI_model

router = APIRouter(prefix="/video")


@router.put("/download/")
async def download_video(video: Video):
    """
    `Video API`
    :param VideoDownload:
    :return video_path:
    """
    try:
        video_path = download_video_(video.url)
        
    except Exception as e:
        raise FailDownloadVideo(ex=e)
    return {"video_path": video_path, "message": f"[영상 다운로드 완료]"}

@router.get("/rename/")
async def rename_video(video: Video):
    """
    `Video API`
    :param VideoRename:
    :return:
    """
    video_ = None
    try:
        video_ = rename_video_(video.path)
    except Exception as e:
        print(f"Error during rename: {e}")
    ...
    return {"video_path": video_[0], "video_title": video_[1], "message": f"[영상 제목 변경 완료]"}


@router.delete("/delete/")
async def delete_video(video: Video):
    """
    `Video API`
    :param VideoDelete:
    :return:
    """
    try:
        delete_video_(video.path)
        print(f"🚩 영상 삭제 완료 : {video.path}")
    except Exception as e:
        print(f"Error during delete: {e}")
    return {"message": f"[영상 삭제 완료]"}

