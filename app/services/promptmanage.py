import os

from app.api.response import SuccessResponse
from app.api import exceptions as ex

from app.common.const import PROMPT_PATH

def load_prompt(file_name):
    try:
        prompt_path = os.path.join(PROMPT_PATH, file_name)
        with open(prompt_path, "r", encoding="utf-8") as f:
            success_message = SuccessResponse()
            print(success_message)
            return f.read()
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)


def load_prompt_path(file_name):
    try:
        prompt_path = os.path.join(PROMPT_PATH, file_name)
        success_message = SuccessResponse()
        print(success_message)
        return prompt_path
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)