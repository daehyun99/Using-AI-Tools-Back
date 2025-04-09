from app.main import create_app
from fastapi.testclient import TestClient

import time
import os
import re


def test_speech2text_integration():
    app = create_app()

    with TestClient(app) as client:
        payload = {
            "url": "https://youtu.be/pVv7qGvhqvg?si=tpk6IxJqZ0-kesan",
            "title": "이_맛에_강아지_키우지"
        }

        response = client.post("/Speech-to-Text/", json=payload)
        assert response.status_code == 200

        cd = response.headers.get("content-disposition", "")
        match = re.search(r"filename\*=utf-8''(.+\.docx)", cd)
        assert match is not None

        filename = match.group(1)

        with open(filename, "wb") as f:
            f.write(response.content)

        assert os.path.exists(filename)
        os.remove(filename)


def test_speech2text_integration_except(): # 잘못된 URL
    app = create_app()

    with TestClient(app) as client:
        payload = {
            "url": "https://www.youtube.com/",
            "title": "잘못된 url"
        }

        response = client.post("/Speech-to-Text/", json=payload)
        assert response.status_code == 200 # HTTP 200이어도 내부 status로 실패 판단

        body = response.json()

        assert body["error"]["code"].startswith("5003")  # 500 (SERVER_ERROR) + 3 (VIDEO) + 001 (Unknown Error)