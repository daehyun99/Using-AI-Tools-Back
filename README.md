# Using-AI-Tools
### [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)
Translate

### [whisperAI](https://github.com/openai/whisper)
Speech to Text

- 구조
```sh

app
├─common
│  └─config.py
├─errors
│  └─exceptions.py
├─routes
│  ├─translate.py
│  └─speech2text.py
├─services
│  └─llm_models.py
├─temp
│  └─videos.py
└─main.py
```

- 환경설정
- [FFmpeg 설치 필요](https://www.ffmpeg.org/download.html)
```sh
# 가상환경 생성
conda create -n AI-tools python=3.10

# 가상환경 활성화
conda activate AI-tools

# 패키지 설치
pip install -y python-dotenv uvicorn fastapi pdf2zh openai-whisper python-docx yt_dlp ffmpeg
# (or) pip install -r requirements.txt
```

### 추가 설정
- .env 생성 및 설정
```

```
- 저장 경로 설정
```
app/tmp/docs
app/tmp/videos
```

### 실행
```
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

- 도커 배포
```
docker build -t kimdaehyun99/fastapi-server:latest --load .

docker run -d -p 8000:8000 kimdaehyun99/fastapi-server:latest
```