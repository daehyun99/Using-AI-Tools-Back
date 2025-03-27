import app.common.config as config
from app.common.config import whisperAI_MODEL_NAME, OPENAI_API_KEY

from openai import OpenAI
import whisper

from app.services.promptmanage import load_prompt

from app.api.response import SuccessResponse
from app.api import exceptions as ex


client = OpenAI(
    api_key=OPENAI_API_KEY
)

whisperAI_model = None

def get_whisper_model():
    if whisperAI_model is None:
        raise ex.ErrorResponse(msg= "🛑 whisper 모델이 아직 로드되지 않았습니다.")
    return whisperAI_model

async def VideoTitleEditer(sentences):
    try:
        prompt = load_prompt("VideoTitleEditer_prompt.txt")
        
        response = client.responses.create(
            model="gpt-4o",
            instructions=f"{prompt}",
            input=f"{sentences}",
        )
        result = response.output_text
        success_message = SuccessResponse()
        print(success_message)
        return result
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)

def WhisperLoader(whisperAI_model):
    try:
        whisperAI_model = whisper.load_model(f"{config.whisperAI_MODEL_NAME}")
        success_message = SuccessResponse(msg= "✅ whisper 모델 로드 성공", data={"model": config.whisperAI_MODEL_NAME})
        print(success_message)
        return whisperAI_model
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)
        return None


async def WhisperUnLoader(whisperAI_model):
    whisperAI_model = None
    success_message = SuccessResponse(msg="✅ whisper 모델 로드 해제")
    print(success_message)
    return None