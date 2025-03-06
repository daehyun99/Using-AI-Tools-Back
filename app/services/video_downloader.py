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
    try:
        os.remove(f'{VIDEO_SAVE_PATH}temp.mp4') # 임시
    except FileNotFoundError:
        print(f"File not found: {VIDEO_SAVE_PATH}temp.mp4")
    except Exception as e:
        print(f"Error deleting video: {e}")

