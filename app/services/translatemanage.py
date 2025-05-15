# from pdf2zh import translate, translate_stream # 현재 Python API을 지원하고 있지 않음.

import os
from app.services.promptmanage import load_prompt_path

from app.common.const import DOCS_SAVE_PATH, TRANSLATE_PROMPT

from app.api.response import SuccessResponse
from app.api import exceptions as ex

import subprocess

from app.common.utils import logging_response

layer = "BUSINESS"

async def translate_(document_path, service, session, correlation_id):
    try:
        if not os.path.exists(DOCS_SAVE_PATH):
            os.makedirs(DOCS_SAVE_PATH)

        if (service == "google") or (service == "deepl"):
            cmd = ["pdf2zh", f"{document_path}", "-s", f"{service}", "-li", "EN", "-lo", "KO", "--output", f"{DOCS_SAVE_PATH}"]

        elif service == "openai":
            prompt_path = load_prompt_path(f"{TRANSLATE_PROMPT}.txt", session=session, correlation_id=correlation_id)
            cmd = ["pdf2zh", f"{document_path}", "-s", f"{service}", "-li", "EN", "-lo", "KO", "--output", f"{DOCS_SAVE_PATH}", "--prompt", f"{prompt_path}"]

        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
