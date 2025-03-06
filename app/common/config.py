import sys, os
from dotenv import load_dotenv

load_dotenv()

DEEPL_API_KEY = os.getenv("DEEPL_API_KEY")

VIDEO_SAVE_PATH = os.getenv("VIDEO_SAVE_PATH", "app/tmp/videos/")

whisperAI_MODEL_NAME = os.getenv("WHISPER_MODEL_NAME", "tiny")

PYTHON_DONT_WRITE_BYTECODE = os.getenv("PYTHON_DONT_WRITE_BYTECODE", "False").lower() == "true"

sys.dont_write_bytecode = PYTHON_DONT_WRITE_BYTECODE