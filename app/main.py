from app.common import config

from typing import Union

import uvicorn
from fastapi import FastAPI
from app.routes import speech2text, translate
from app.services.llm_models import lifespan

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI(lifespan=lifespan)
    
    # 미들웨어 정의


    
    # 라우터 정의
    app.include_router(translate.router, tags=["Translate"])
    app.include_router(speech2text.router, tags=["Speech to Text"])

    return app




app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)