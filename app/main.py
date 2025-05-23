import uvicorn
from fastapi import FastAPI
from typing import Union

from fastapi.middleware.cors import CORSMiddleware

from app.routes import PipeLine
from app.common.lifespan import lifespan
from app.common.config import conf, ENV
from app.common.logger import logger


# 개발용
from app.routes import VideoManager, FileManager, TranslateManager, EmailManager


def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI(lifespan=lifespan)

    


    # 미들웨어 정의
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["http://localhost:5173"],  # Vite 개발 서버 주소
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )




    # 개발용 라우터 정의
    if ENV == "development": 
        app.include_router(VideoManager.router, tags=["VideoManager"])
        app.include_router(FileManager.router, tags=["FileManager"])
        app.include_router(EmailManager.router, tags=["EmailManager"])
        app.include_router(PipeLine.router, tags=["PipeLine"])
        app.include_router(TranslateManager.router, tags=["Translate"])

    # 배포용, 테스트용 라우터 정의
    elif ENV == "production" or ENV == "test": 
        app.include_router(PipeLine.router, tags=["PipeLine"])
    
    
    logger.info("✅ App created.")
    return app




app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)