import os
import re

import yt_dlp
from app.common.config import VIDEO_SAVE_PATH, base_dir


def download_video(video_url, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    ydl_opts = {
        'outtmpl': f'{VIDEO_SAVE_PATH}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_ = ydl.extract_info(video_url, download=True)
            video_title = info_.get('title', None)
            video_ext = info_.get('ext', None)
            # 영상 파일 생성 기다리기
            import time
            time.sleep(5)


            if video_title and video_ext:
                return f"{VIDEO_SAVE_PATH}/{video_title}.{video_ext}"
            else:
                raise Exception("Could not retrieve video title or extension")
    
    except Exception as e:
        raise e
        
def delete_video(video_path, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    try:
        os.remove(f'{video_path}')
    except FileNotFoundError:
        print(f"File not found: {video_path}")
    except Exception as e:
        print(f"Error deleting video: {e}")


def rename_video(video_path, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH):
    """
    영상(video)의 제목(title)에 큰따옴표(") 또는 처리 불가능한 문자(ex - “)가 있는 경우, whisper 모델에서 처리 불가한 문제 발생.
    해당 문제를 해결하기 위해 영상의 제목을 변경하는 함수.

    버그 재현 :
        - video title : 시가총액 1위 '엔비디아'의 시작도 초라했다 "불품없어도 시작해야하는 이유“
        - video url : https://youtube.com/shorts/xPTh2lYQN6w?si=IpYGBDE1E39VsPVv
    """
    ...
    # return video_path
    
    