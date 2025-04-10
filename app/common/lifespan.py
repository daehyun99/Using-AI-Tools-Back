from dataclasses import asdict

from app.database.conn import db

from app.common.config import conf

from contextlib import asynccontextmanager
from app.api.response import SuccessResponse
from app.api import exceptions as ex

@asynccontextmanager
async def lifespan(app):
    try:
        conf_dict = asdict(conf())
        db.init_app(app, **conf_dict)
        
        yield
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)
        yield
    finally:
        db.close()