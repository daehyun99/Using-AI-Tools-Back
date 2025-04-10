from dataclasses import dataclass

from os import path, environ, getenv
from dotenv import load_dotenv

base_dir = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

# ================================================================================ #
# .ENV

load_dotenv()

# "production" or "development"
ENV = getenv("ENV", "development") 

# API keys
DEEPL_AUTH_KEY = getenv("DEEPL_AUTH_KEY")
OPENAI_API_KEY = getenv("OPENAI_API_KEY")

# Models
OPENAI_MODEL = getenv("OPENAI_MODEL", "gpt-4o")
whisperAI_MODEL_NAME = getenv("WHISPER_MODEL_NAME", "tiny")

# Databases
DB_USER = getenv("DB_USER")
DB_PW = getenv("DB_PW")
DB_HOST = getenv("DB_HOST")
DB_PORT = getenv("DB_PORT")
DB_NAME = getenv("DB_NAME")

# E-mail
test_receiver = getenv("EMAIL_RECEIVER_TEST")
sender = getenv("EMAIL_SENDER")
smtp_server = getenv("SMTP_SERVER")
smtp_port = getenv("SMTP_PORT")
login_id = getenv("EMAIL_LOGIN_ID")
login_pw = getenv("EMAIL_LOGIN_PW")
survey_form_url = getenv("SURVEY_FORM_URL")

# ================================================================================ #
# Databases

@dataclass
class Config:
    BASE_DIR = base_dir
    
    DB_POOL_RECYCLE: int = 900
    DB_ECHO: bool = True


@dataclass
class DevConfig(Config):
    DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


@dataclass
class ProbConfig(Config):
    DB_URL: str = getenv("DB_URL", f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4")
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]

@dataclass
class TestConfig(Config):
    DB_URL: str = f"mysql+pymysql://{DB_USER}:{DB_PW}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8mb4"
    TRUSTED_HOSTS = ["*"]
    ALLOW_SITE = ["*"]


def conf():
    """
    환경 불러오기
    :return:
    """
    config = dict(production=ProbConfig(), development=DevConfig(), test=TestConfig())
    return config.get(ENV, DevConfig())