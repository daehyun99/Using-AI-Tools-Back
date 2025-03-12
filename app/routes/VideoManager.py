from fastapi import APIRouter

<<<<<<< HEAD
from app.models import VideoRename, VideoDownload, VideoDelete
=======
from app.models import Video
>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
from app.services.videomanage import download_video, delete_video, rename_video
from app.common.config import VIDEO_SAVE_PATH, DOCS_SAVE_PATH

from app.errors.exceptions import APIException, FailDownloadVideo

from app.services.llm_models import whisperAI_model

router = APIRouter(prefix="/video")


@router.put("/download/")
<<<<<<< HEAD
async def download(video: VideoDownload):
=======
async def download(video: Video):
>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
    """
    `Video API`
    :param VideoDownload:
    :return video_path:
    """
    try:
        video_path = download_video(video.url)
        
    except Exception as e:
        raise FailDownloadVideo(ex=e)
<<<<<<< HEAD
    return f"[영상 다운로드 완료] path : {video_path}"

@router.get("/rename")
def rename(video: VideoRename):
=======
    return {"video_path": video_path, "message": f"[영상 다운로드 완료]"}

@router.get("/rename")
async def rename(video: Video):
>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
    """
    `Video API`
    :param VideoRename:
    :return:
    """
<<<<<<< HEAD
    try:
        video_path = rename_video(video.path)
    except Exception as e:
        print(f"Error during rename: {e}")
    ...
    return f"[영상 제목 변경 완료] path : {video.path}"


@router.delete("/delete/")
async def delete(video: VideoDelete):
=======
    video_ = None
    try:
        video_ = rename_video(video.path)
    except Exception as e:
        print(f"Error during rename: {e}")
    ...
    return {"video_path": video_[0], "video_title": video_[1], "message": f"[영상 제목 변경 완료]"}


@router.delete("/delete/")
async def delete(video: Video):
>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
    """
    `Video API`
    :param VideoDelete:
    :return:
    """
    try:
        delete_video(video.path)
        print(f"🚩 영상 삭제 완료 : {video.path}")
    except Exception as e:
        print(f"Error during delete: {e}")
<<<<<<< HEAD
    return f"[영상 삭제 완료] path : {video.path}"
=======
    return {"message": f"[영상 삭제 완료]"}

>>>>>>> 9fa9f9d (Feat: 파이프라인 작성(Speech-to-Text))
