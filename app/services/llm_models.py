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
    # prompt = load_prompt("VideoTitleEditer_prompt.txt")
    # print(prompt)
    prompt="""당신은 유튜브 영상 제목을 자동으로 수정하는 AI입니다.
    사용자가 제공한 제목에서 빈 칸, 큰따옴표("), 특수 문자(“) 등을 제거하고, 의미는 유지하면서 자연스럽게 수정하세요.
    가능한 한 원본 제목과 유사한 형태를 유지하되, 필요한 경우 대체 문자를 사용하세요."""
    try:
        response = client.responses.create(
            model="gpt-4o",
            instructions=f"{prompt}",
            input=f"{sentences}",
        )
        result = response.output_text
    except Exception as e:
        print(f"ERROR : {e}")
        result = sentences
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