from app.common.config import whisperAI_MODEL_NAME, OPENAI_API_KEY

import sys
from openai import OpenAI
import whisper
import whisper.utils

from app.services.promptmanage import load_prompt
from app.errors import exceptions as ex
from app.errors.exceptions import APIException, FailLoadLLM


from contextlib import asynccontextmanager

client = OpenAI(
    api_key=OPENAI_API_KEY
)

whisperAI_model = None

def get_whisper_model():
    if whisperAI_model is None:
        raise RuntimeError("🚨 whisper 모델이 아직 로드되지 않았습니다.")
    return whisperAI_model

async def VideoTitleEditer(sentences):
    prompt = load_prompt("VideoTitleEditer_prompt.txt")
    
    response = client.responses.create(
        model="gpt-4o",
        instructions=f"{prompt}",
        input=f"{sentences}",
    )
    result = response.output_text
    return result


@asynccontextmanager
async def lifespan(app):
    global whisperAI_model
    try:
        # whisperAI_MODEL_NAME = "except_test" # LLM 모델 로드 실패 테스트 코드
        whisperAI_model = whisper.load_model(f"{whisperAI_MODEL_NAME}")
        print("🚩 whisper 모델 로드")
        yield
    except Exception as e:
        raise ex.FailLoadLLM()
    finally:
        whisperAI_model = None
        print("🚩 whisper 모델 로드 해제")