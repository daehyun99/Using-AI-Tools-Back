import sys, os
from os import path, environ
from dotenv import load_dotenv

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


load_dotenv()

ENV = os.getenv("ENV", "development") # "production" or "development"

DEEPL_AUTH_KEY = os.getenv("DEEPL_AUTH_KEY")

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

OPENAI_BASE_URL = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")

OPENAI_MODEL = os.getenv("OPENAI_MODEL", "gpt-4o")

VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", "app/tmp/videos/")

DOCS_SAVE_PATH = os.getenv("DOCS_SAVE_PATH", "app/tmp/docs/")

PROMPT_PATH = os.getenv("PROMPT_PATH", "app/prompt/")

whisperAI_MODEL_NAME = os.getenv("WHISPER_MODEL_NAME", "tiny")

PYTHON_DONT_WRITE_BYTECODE = os.getenv("PYTHON_DONT_WRITE_BYTECODE", "False").lower() == "true"

sys.dont_write_bytecode = PYTHON_DONT_WRITE_BYTECODE