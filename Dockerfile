FROM python:3.10-slim

RUN apt-get update && \
    apt-get install -y locales ffmpeg build-essential python3-dev iputils-ping && \
    echo "ko_KR.UTF-8 UTF-8" > /etc/locale.gen && \
    locale-gen ko_KR.UTF-8 && \
    rm -rf /var/lib/apt/lists/*

ENV LANG=ko_KR.UTF-8
ENV LANGUAGE=ko_KR:ko
ENV LC_ALL=ko_KR.UTF-8

WORKDIR /app

COPY requirements.txt /app/requirements.txt

RUN pip install --upgrade pip setuptools wheel && \
    pip install --no-cache-dir -r requirements.txt

COPY . /app

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

# development
# CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]