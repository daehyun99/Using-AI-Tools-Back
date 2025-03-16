import os

from app.common.config import PROMPT_PATH

def load_prompt(file_name):
    prompt_path = os.path.join(PROMPT_PATH, file_name)
    with open(prompt_path, "r", encoding="utf-8") as f:
        return f.read()

def load_prompt_path(file_name):
    prompt_path = os.path.join(PROMPT_PATH, file_name)
    return prompt_path
