from fastapi import APIRouter
from typing import Union

from app.services.llm_models import whisperAI_model

from app.models import VideoURL
from app.services.video_downloader import download_video, delete_video

from app.errors.exceptions import APIException, FailDownloadVideo


router = APIRouter()

# <======================>
# # Todo
# 진행상황
# |✅: 완료|⏩: 진행 중|⏸: 중단|⚪: 대기|
# ⏩ 1. video_url의 video 영상 다운로드
# ⚪ 2. whisperAI 모델 cahce 필요
# ⚪ (+) 모델 사이즈 변경 필요 

# # 관련
# python-docx, ffmpeg, yt_dlp
# ========================

# <======================>
# # UseCase
# 1. 사용자는 video_url를 입력한다.
# 2. 시스템은 해당 url의 video를 다운로드한다.
# 3. 시스템은 해당 video의 speech2text를 수행한다.
# 3. 시스템은 speech2text를 수행한 (Word or PDF) 파일을 제공한다.
# ========================

@router.put("/download/")
async def whisper(video_url: VideoURL):
    """
    Speech2Text API
    :param video_url: video url
    :return: DOCS
    """
    
    # 모델 로드 확인

    # video 다운로드(temp)
    try:
        print(f"🚩 영상 다운로드 시작 : {video_url.url}")
        download_video(video_url.url)
    except Exception as e:
        print(f"Error during download: {e}") # Log the exception
        raise FailDownloadVideo(ex=e)

    
    # speech2text 수행

    # video 삭제(temp)
    
    # 영상 삭제 테스트용 코드
    # import time
    # time.sleep(5)
    try:
        delete_video(video_url.url)
        print(f"🚩 영상 삭제 완료 : {video_url.url}")
        raise FailDeleteVideo(ex=e)



    # (Word or PDF) 파일 제공


# # ===============
# # test code
from typing import Union

@router.get("/speech2text")
def speech2text_test1():
    return {"Hello": "World"}

@router.get("/speech2text/items/{item_id}")
def speech2text_test2(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}