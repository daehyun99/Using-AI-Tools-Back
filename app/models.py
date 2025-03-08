from typing import Optional
from pydantic import BaseModel, Field


class VideoDownload(BaseModel):
    """Video 다운로드용 모델"""
    url: Optional[str] = None


class VideoDelete(BaseModel):
    """Video 삭제용 모델"""
    path: Optional[str] = None
