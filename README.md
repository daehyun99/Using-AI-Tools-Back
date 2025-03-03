# Using-AI-Tools
### [PDFMathTranslate](https://github.com/Byaidu/PDFMathTranslate)
Translate

### [whisperAI](https://github.com/openai/whisper)
Speech to Text

- 구조
```sh
main.py
app
├─common
│  └─config.py
└─routes
   └─translate.py

```

- 환경설정
```sh
# 가상환경 생성
conda create -n AI-tools python=3.10

# 가상환경 활성화
conda activate AI-tools

# 패키지 설치
pip install python-dotenv uvicorn fastapi

# 실행
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```