from dataclasses import asdict

from app.database.conn import db

from app.common.config import conf
from app.common.logger import logger

from contextlib import asynccontextmanager
from app.services.llm_models import WhisperLoader, WhisperUnLoader
from app.api.response import SuccessResponse
from app.api import exceptions as ex

whisperAI_model = None

@asynccontextmanager
async def lifespan(app):
    global whisperAI_model
    try:
        conf_dict = asdict(conf())
        db.init_app(app, **conf_dict)
        
        whisperAI_model = WhisperLoader(whisperAI_model= whisperAI_model)
        logger.info("✅ Lifespan startup complete")
        yield
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)
        yield
    finally:
        whisperAI_model = WhisperUnLoader(whisperAI_model= whisperAI_model)
        db.close()
        logger.info("✅ Lifespan shutdown complete")