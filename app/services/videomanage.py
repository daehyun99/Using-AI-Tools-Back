import os
import re

import yt_dlp
from app.common.config import base_dir
from app.common.const import VIDEO_SAVE_PATH
from app.services.llm_models import VideoTitleEditer
from app.api.response import SuccessResponse
from app.api import exceptions as ex

from app.common.utils import logging_response

layer = "BUSINESS"

def download_video_(video_url, session, correlation_id, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    try:
        # logging_request
        ydl_opts = {
            'outtmpl': f'{VIDEO_SAVE_PATH}/temp_{correlation_id}.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_ = ydl.extract_info(video_url, download=True)
            video_title = info_.get('title', None)
            video_ext = info_.get('ext', None)
            # 영상 파일 생성 기다리기
            import time
            time.sleep(5)

            if video_title and video_ext:
                data = f"{VIDEO_SAVE_PATH}/{video_title}.{video_ext}"
                success_message = SuccessResponse(data=data)
                return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
            else:
                error_message = ex.ErrorResponse(ex=e)
                return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
    
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)
        

def delete_video_(video_path, session, correlation_id, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    try:
        os.remove(f'{video_path}')
        success_message = SuccessResponse()
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)

async def rename_video_(video_path, session, correlation_id, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH):
    try:
        base_name = os.path.basename(video_path)
        video_title, video_ext = os.path.splitext(base_name)
        video_title = video_title.encode('utf-8').decode('utf-8')
        video_title = re.sub(r'[\\/*?:"<>|]', '', video_title).strip()
        new_video_title = await VideoTitleEditer(sentences = video_title, session=session, correlation_id=correlation_id)
        new_video_path = os.path.join(VIDEO_SAVE_PATH, f"{new_video_title}{video_ext}")
        os.rename(f'{VIDEO_SAVE_PATH}/temp_{correlation_id}{video_ext}', new_video_path)        
        success_message = SuccessResponse(data={"video_path": new_video_path, "video_title": new_video_title})
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        return logging_response(session=session, layer=layer, correlation_id=correlation_id, obj=error_message)