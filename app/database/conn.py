from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from app.api import exceptions as ex

from app.common.logger import logger


class SQLAlchemy:
    def __init__(self, app: FastAPI = None, **kwargs):
        self._engine = None
        self._session = None
        if app is not None:
            self.init_app(app=app, **kwargs)

    def init_app(self, app: FastAPI = None, **kwargs):
        """
        DB 초기화 함수
        :param app:
        :return:
        """
        database_url = kwargs.get("DB_URL")
        pool_recycle = kwargs.setdefault("DB_POOL_RECYCLE", 900)
        echo = kwargs.setdefault("DB_ECHO", True)

        self._engine = create_engine(
            database_url,
            echo=echo,
            pool_recycle=pool_recycle,
            pool_pre_ping=True,
        )

        self._session = sessionmaker(autocommit=False, autoflush=False, bind=self._engine)
        db._engine.connect()
        logger.info("✅ DB connected")
        
    def get_db(self):
        """
        요청마다 DB 세션 유지 함수
        :return:
        """
        try:
            if self._session is None:
                error_message = ex.ErrorResponse()
                print(error_message)
            db_session = None
        except:
            ...
        try:
            db_session = self._session()
            yield db_session
        except Exception as e:
            error_message = ex.ErrorResponse(ex=e)
            print(error_message)
        finally:
            db_session.close()
    
    def close(self) -> None:
        """
        DB 연결 해제 함수
        :return:
        """
        db._session.close_all()
        db._engine.dispose()
        logger.info("✅ DB disconnected")
        

    @property
    def session(self):
        return self.get_db
    
    @property
    def engine(self):
        return self._engine
    
db = SQLAlchemy()
Base = declarative_base()
