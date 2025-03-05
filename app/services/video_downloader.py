import yt_dlp


def download_video(video_url, save_path="./"):
    ydl_opts = {
        'outtmpl': f'{save_path}/temp.%(ext)s',
    }
    with yt_dlp.YoutubeDL() as ydl:
        ydl.download([video_url])
        


