import app.common.config as config
from app.common.config import whisperAI_MODEL_NAME, OPENAI_API_KEY

from openai import OpenAI
import whisper

from app.services.promptmanage import load_prompt

from app.database.conn import db

from app.api.response import SuccessResponse
from app.api import exceptions as ex

from app.common.utils import generate_metadata
from app.common.utils import logging_response

layer = "BUSINESS"

client = OpenAI(
    api_key=OPENAI_API_KEY
)


def get_whisper_model(whisperAI_model, session, correlation_id):
    if whisperAI_model is None:
        error_message = ex.ErrorResponse_LLM()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    return whisperAI_model

async def VideoTitleEditer(sentences, session, correlation_id):
    try:
        prompt = load_prompt("VideoTitleEditer_prompt002.txt", session, correlation_id)
        
        response = client.responses.create(
            model="gpt-4o",
            instructions=f"{prompt}",
            input=f"{sentences}",
        )
        result = response.output_text
        success_message = SuccessResponse()
        print("test", success_message)
        return result
    except Exception as e:
        error_message = ex.ErrorResponse_LLM(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)

def WhisperLoader(whisperAI_model):
    try:
        session = next(db.session())
        correlation_id = generate_metadata()
        # logging_request
        whisperAI_model = whisper.load_model(f"{config.whisperAI_MODEL_NAME}")
        success_message = SuccessResponse(msg= "✅ whisper 모델 로드 성공", data={"model": config.whisperAI_MODEL_NAME})
        print(success_message)
        return whisperAI_model
    except Exception as e:
        error_message = ex.ErrorResponse_LLM(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)


def WhisperUnLoader(whisperAI_model):
    session = next(db.session())
    correlation_id = generate_metadata()
    # logging_request
    whisperAI_model = None
    success_message = SuccessResponse(msg="✅ whisper 모델 로드 해제")
    print(success_message)
    return None