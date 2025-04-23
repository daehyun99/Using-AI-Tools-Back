# Using-AI-Tools ![Dev](https://img.shields.io/badge/Dev-red)
## Front-end
[![Frontend Repo](https://img.shields.io/badge/Frontend-Using--AI--Tools--Front-blue?logo=github)](https://github.com/daehyun99/Using-AI-Tools-Front)

## Back-end
![Python](https://img.shields.io/badge/python-3.10.16-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-%2300C7B7.svg?&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-blue?logo=docker)
![MySQL](https://img.shields.io/badge/MySQL-005C84?logo=mysql)

[![GitHub repo](https://img.shields.io/badge/ref-fastapi--mcp-black?logo=github)](https://github.com/tadata-org/fastapi_mcp)
[![PDFMathTranslate](https://img.shields.io/badge/ref-PDFMathTranslate-blue?logo=github)](https://github.com/Byaidu/PDFMathTranslate)
[![whisperAI](https://img.shields.io/badge/ref-whisperAI-green?logo=github)](https://github.com/openai/whisper)

![GPT API](https://img.shields.io/badge/GPT--API-FFB6C1?logo=openai)
![DeepL API](https://img.shields.io/badge/DeepL%20API-blue?logo=deepl)

## Diagram
```mermaid
graph TD
    User[User] <-->|Using-AI-Tools-Front| AI_Agent[AI Agent]
    AI_Agent[AI Agent] -->|calls| ENTRY[System Entry]

    subgraph fastapi-mcp
        ENTRY --> 음성[영어 영상.mp4]
        ENTRY --> 텍스트[영어 논문.pdf]
        음성 --> whisperAI[whisperAI]
        whisperAI -->|Speech to Text| 영어텍스트[영어 text]
        텍스트 --> 영어텍스트
        영어텍스트 --> PDFMathTranslate
        PDFMathTranslate --> 한글텍스트[한글 자막 or 번역 논문]
    end

    한글텍스트 -->|output| AI_Agent
```

## Documents
- [wiki](http://github.com/daehyun99/Using-AI-Tools/wiki)
- [통합 wiki (v1.0.0)](https://github.com/daehyun99/Translate-app/wiki/Back-end)

## 실행
```sh
uvicorn app.main:app --host 127.0.0.1 --port 8000 --reload
```
