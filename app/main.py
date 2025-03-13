from app.common import config
from app.common.config import ENV

from typing import Union

import uvicorn
from fastapi import FastAPI
from app.routes import PipeLine
from app.services.llm_models import lifespan

# 개발용
from app.routes import Translater, VideoManager, FileManager


def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI(lifespan=lifespan)
    
    # 미들웨어 정의





    # 개발용 라우터 정의
    if ENV == "development": 
        app.include_router(VideoManager.router, tags=["VideoManager"])
        app.include_router(FileManager.router, tags=["FileManager"])
        app.include_router(PipeLine.router, tags=["PipeLine"])
        # app.include_router(Translater.router, tags=["Translate"])

    # 배포용 라우터 정의
    elif ENV == "production": 
        # app.include_router(PipeLine.router, tags=["PipeLine"])
        ...
    

    return app




app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)