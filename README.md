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
├─routes
│  ├─translate.py
│  └─speech2text.py
├─services
│  └─llm_models.py
└─main.py
```

- 환경설정
```sh
# 가상환경 생성
conda create -n AI-tools python=3.10

# 가상환경 활성화
conda activate AI-tools

# 패키지 설치
pip install python-dotenv uvicorn fastapi

# Speech-to-Text
pip install python-docx ffmpeg yt_dlp

# 실행
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```

- whisperAI 관련 환경 설정
```sh
cd USING-AI-TOOLS
pip install ./whisperAI

# or

# pip install -U openai-whisper
```

- PDFMathTranslate 관련 환경 설정
```sh
cd USING-AI-TOOLS
pip install ./PDFMathTranslate

# or

# pip install pdf2zh
```