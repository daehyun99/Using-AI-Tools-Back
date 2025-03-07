# 베이스 이미지로 Python 3.9 slim 사용
FROM python:3.10-slim

# 시스템 패키지 업데이트 및 ffmpeg 설치, 캐시 정리
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    rm -rf /var/lib/apt/lists/*

# 작업 디렉터리 설정
WORKDIR /app

# requirements.txt 복사 후 라이브러리 설치
COPY requirements.txt /app/requirements.txt
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# 애플리케이션 소스 코드 복사
COPY . /app

# 필요한 포트 노출 (예: 8000)
EXPOSE 8000

# uvicorn을 사용하여 FastAPI 애플리케이션 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
