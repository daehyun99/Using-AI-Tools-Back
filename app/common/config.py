import sys, os
from os import path, environ
from dotenv import load_dotenv

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


load_dotenv()

ENV = os.getenv("ENV", "development") # "production" or "development"

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", "app/tmp/videos/")
# VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", f"{base_dir}/app/tmp/videos/")
DOCS_SAVE_PATH = os.getenv("DOCS_SAVE_PATH", "app/tmp/docs/")

whisperAI_MODEL_NAME = os.getenv("WHISPER_MODEL_NAME", "tiny")

PYTHON_DONT_WRITE_BYTECODE = os.getenv("PYTHON_DONT_WRITE_BYTECODE", "False").lower() == "true"

sys.dont_write_bytecode = PYTHON_DONT_WRITE_BYTECODE