from typing import Union

import uvicorn
from fastapi import FastAPI

from app.common import config
from app.routes import translate

def create_app():
    """
    앱 함수 실행
    :return:
    """
    app = FastAPI()
    
    # 라우터 정의
    app.include_router(translate.router, tags=["Translate"])

    return app




app = create_app()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)