import os

import yt_dlp
from app.common.config import VIDEO_SAVE_PATH


def download_video(video_url, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    ydl_opts = {
        # 'outtmpl': f'{VIDEO_SAVE_PATH}temp.%(ext)s',
        'outtmpl': f'{VIDEO_SAVE_PATH}/%(title)s.%(ext)s',
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_ = ydl.extract_info(video_url, download=True)
            # ydl.download([video_url])
            video_title = info_.get('title', None)
            video_ext = info_.get('ext', None)

            if video_title and video_ext:
                return f"{VIDEO_SAVE_PATH}/{video_title}.{video_ext}"
            else:
                raise Exception("Could not retrieve video title or extension")
    
    except Exception as e:
        raise e
        
def delete_video(video_url, VIDEO_SAVE_PATH=VIDEO_SAVE_PATH): 
    try:
        os.remove(f'{VIDEO_SAVE_PATH}temp.mp4') # 임시
    except FileNotFoundError:
        print(f"File not found: {VIDEO_SAVE_PATH}temp.mp4")
    except Exception as e:
        print(f"Error deleting video: {e}")

