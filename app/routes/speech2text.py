from fastapi import APIRouter
from typing import Union
from docx import Document

from app.services.llm_models import whisperAI_model

from app.models import VideoURL
from app.common.config import VIDEO_SAVE_PATH, DOCS_SAVE_PATH
from app.services.video_downloader import download_video, delete_video

from app.errors.exceptions import APIException, FailDownloadVideo, FailDeleteVideo


router = APIRouter(prefix="/speech2text")

# <======================>
# # Todo
# 진행상황
# |✅: 완료|⏩: 진행 중|⏸: 중단|⚪: 대기|
# ✅ 1. video_url의 video 영상 다운로드
# ✅ 2. whisperAI 모델 cahce 필요 (자동 지정)
# ✅ 3. speech2text 수행
# ⚪ 4. 저장할 파일명 지정
# ⚪ 4. (Word or PDF) 형태로 파일 저장
# ⚪ 5. 저장된 파일을 사용자에게 제공
# ✅ . video 영상 삭제
# ⚪ (+) 로깅 기능 추가
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
    import whisper
    whisperAI_model = whisper.load_model("tiny")  # 혹은 적절한 로딩 함수

    # video 다운로드(temp)
    try:
        print(f"🚩 영상 다운로드 시작 : {video_url.url}")
        video_path = download_video(video_url.url)
    except Exception as e:
        print(f"Error during download: {e}") # Log the exception
        raise FailDownloadVideo(ex=e)

    import time
    time.sleep(10)
    
    # speech2text 수행
    result = whisperAI_model.transcribe(video_path, task="transcribe")


    doc = Document()
    doc.add_paragraph(result['text'])
    doc.save(f"{DOCS_SAVE_PATH}/test_result.docx")
    # video 삭제(temp)
    
    # 영상 삭제 테스트용 코드
    # import time
    # time.sleep(5)
    # try:
    #     delete_video(video_url.url)
    #     print(f"🚩 영상 삭제 완료 : {video_url.url}")
    # except Exception as e:
    #     print(f"Error during delete: {e}") # Log the exception
    #     # raise FailDeleteVideo(ex=e)



    # (Word or PDF) 파일 제공


# # ===============
# # test code
from typing import Union

@router.get("/get-test")
def speech2text_test1():
    return {"Hello": "World"}

@router.get("/item-test/{item_id}")
def speech2text_test2(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}