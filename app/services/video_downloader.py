import os

import yt_dlp
from app.common.config import VIDEO_SAVE_PATH


def download_video(video_url, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    ydl_opts = {
        'outtmpl': f'{VIDEO_SAVE_PATH}temp.%(ext)s',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])
        
def delete_video(video_url, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    # os.remove(f'{VIDEO_SAVE_PATH}temp.%(ext)s') # 확장자명 처리 방법 고민
    os.remove(f'{VIDEO_SAVE_PATH}temp.mp4') # 임시

