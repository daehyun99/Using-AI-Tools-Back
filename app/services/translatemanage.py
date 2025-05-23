# from pdf2zh import translate, translate_stream # 현재 Python API을 지원하고 있지 않음.

import os
from app.services.promptmanage import load_prompt_path

from app.api.response import SuccessResponse
from app.api import exceptions as ex

import subprocess

from app.common.utils import logging_response

layer = "BUSINESS"

async def translate_(document_path, service, session, correlation_id):
    try:
        base_name = os.path.basename(document_path)
        document_title, document_ext = os.path.splitext(base_name)

        output_dir = "app/tmp/docs/"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        if (service == "google") or (service == "deepl"):
            cmd = ["pdf2zh", f"{document_path}", "-s", f"{service}", "-li", "EN", "-lo", "KO", "--output", f"{output_dir}"]

        elif service == "openai":
            prompt_path = load_prompt_path("translate__prompt003.txt", session=session, correlation_id=correlation_id)
            cmd = ["pdf2zh", f"{document_path}", "-s", f"{service}", "-li", "EN", "-lo", "KO", "--output", f"{output_dir}", "--prompt", f"{prompt_path}"]

        result = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8")

        mono_document_title_ext = f"{document_title}" + "-mono" + f"{document_ext}"
        dual_document_title_ext = f"{document_title}" + "-dual" + f"{document_ext}"

        new_document_path = os.path.join(f"{output_dir}", mono_document_title_ext)
        success_message = SuccessResponse()
        return mono_document_title_ext, dual_document_title_ext, new_document_path
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
