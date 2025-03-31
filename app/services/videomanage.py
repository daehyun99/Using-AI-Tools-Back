import os
import re

import yt_dlp
from app.common.config import base_dir
from app.common.const import VIDEO_SAVE_PATH
from app.services.llm_models import VideoTitleEditer
from app.api.response import SuccessResponse
from app.api import exceptions as ex

from app.services.utils import logging_response

def download_video_(video_url, session, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH, ): 
    try:
        # logging_request
        ydl_opts = {
            'outtmpl': f'{VIDEO_SAVE_PATH}/%(title)s.%(ext)s',
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
                return logging_response(session= session, correlation_id="correlation_id", obj=success_message)
            else:
                ...
                error_message = ex.ErrorResponse(ex=e)
                print(error_message)
                return logging_response(session= session, correlation_id="correlation_id", obj=error_message)
    
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)
        return logging_response(session= session, correlation_id="correlation_id", obj=error_message)
        

def delete_video_(video_path, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    try:
        os.remove(f'{video_path}')
        success_message = SuccessResponse()
        print(success_message)
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)

async def rename_video_(video_path, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH):
    """
    영상(video)의 제목(title)에 큰따옴표(") 또는 처리 불가능한 문자(ex - “)가 있는 경우, whisper 모델에서 처리 불가한 문제 발생.
    해당 문제를 해결하기 위해 영상의 제목을 변경하는 함수.

    관련 링크 :
        - 이슈 이름 :유튜브 영상 제목 변경 시 오류 발생 #9
        - 링크 : https://github.com/daehyun99/Using-AI-Tools/issues/9
    """
    try:
        base_name = os.path.basename(video_path)
        video_title, video_ext = os.path.splitext(base_name)
        video_title = video_title.encode('utf-8').decode('utf-8')
        video_title = re.sub(r'[\\/*?:"<>|]', '', video_title).strip()
        new_video_title = await VideoTitleEditer(sentences = video_title)
        new_video_path = os.path.join(VIDEO_SAVE_PATH, f"{new_video_title}{video_ext}")
        os.rename(video_path, new_video_path)
        success_message = SuccessResponse()
        print(success_message)
        return [new_video_path, new_video_title]
    except Exception as e:
        error_message = ex.ErrorResponse(ex=e)
        print(error_message)