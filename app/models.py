from typing import Optional
from enum import Enum

from pydantic import BaseModel, Field


class Video(BaseModel):
    """Video Speech-to-Text용 모델"""
    url: Optional[str] = None
    path: Optional[str] = None
    title: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "url": "https://www.youtube.com/"
            }
        }

class Document_(BaseModel):
    """Document 반환용 모델"""
    path: Optional[str] = None

    class Config:
        json_schema_extra = {
            "example": {
                "path": "app/tmp/docs/test_result.docx"
            }
        }

class TranslateService(str, Enum):
    """Translate 서비스 모델"""
    google = "google"
    deepl = "deepl"
    openai = "openai"
