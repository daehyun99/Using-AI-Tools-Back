from typing import Optional
from pydantic import BaseModel


class VideoURL(BaseModel):
    url: Optional[str] = None