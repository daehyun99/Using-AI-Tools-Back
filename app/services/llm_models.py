from app.common.config import whisperAI_MODEL_NAME

import sys
import whisperAI
import whisperAI.whisper
import whisperAI.whisper.utils

from app.errors import exceptions as ex
from app.errors.exceptions import APIException, FailLoadLLM


from contextlib import asynccontextmanager

whisperAI_model = None

@asynccontextmanager
async def lifespan(app):
    global whisperAI_model
    try:
        # whisperAI_MODEL_NAME = "except_test" # LLM 모델 로드 실패 테스트 코드
        whisperAI_model = whisperAI.whisper.load_model(f"{whisperAI_MODEL_NAME}")
        print("🚩 whisper 모델 로드")
    except Exception as e:
        whisperAI_model = None
        raise ex.FailLoadLLM()

    yield
    whisperAI_model = None
    print("🚩 whisper 모델 로드 해제")