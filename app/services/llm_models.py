from app.common.config import whisperAI_MODEL_NAME

import whisperAI
import whisperAI.whisper
import whisperAI.whisper.utils

from contextlib import asynccontextmanager

whisperAI_model = None  # 전역 변수로 선언

@asynccontextmanager
async def lifespan(app):
    print("🔥 WhisperAI 모델 로드 시작!")
    global whisperAI_model
    try:
        whisperAI_model = whisperAI.whisper.load_model(f"{whisperAI_MODEL_NAME}")
        print("🔥 WhisperAI 모델 로드 완료!")
    except Exception as e:
        print(f"🛑 WhisperAI 모델 로드 실패: {e}")
        # Consider raising the exception or taking other appropriate action
        whisperAI_model = None
    print("🔥 WhisperAI 모델 로드 완료!")
    yield
    whisperAI_model = None
    print("🛑 WhisperAI 모델 언로드 완료!")
