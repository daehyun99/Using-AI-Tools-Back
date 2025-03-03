from fastapi import APIRouter
from typing import Union

from app.services.llm_models import whisperAI_model


router = APIRouter()

# <======================>
# # Todo
# 진행상황
# |✅: 완료|⏩: 진행 중|⏸: 중단|⚪: 대기|
# ⏩ 1. video_url의 video 영상 다운로드
# ⚪ 2. whisperAI 모델 cahce 필요
# ⚪ (+) 모델 사이즈 변경 필요 

# # 관련
# python-docx, ffmpeg
# ========================

# <======================>
# # UseCase
# 1. 사용자는 video_url를 입력한다.
# 2. 시스템은 해당 url의 video를 다운로드한다.
# 3. 시스템은 해당 video의 speech2text를 수행한다.
# 3. 시스템은 speech2text를 수행한 (Word or PDF) 파일을 제공한다.
# ========================

# @router
# async def whisper():
    
#     # video_url 확인

#     # 모델 로드 확인

#     # video 다운로드

#     # speech2text 수행

#     # (Word or PDF) 파일 제공


# # ===============
# # test code
from typing import Union

@router.get("/speech2text")
def speech2text_test1():
    return {"Hello": "World"}

@router.get("/speech2text/items/{item_id}")
def speech2text_test2(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}