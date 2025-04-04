from app.main import create_app
from fastapi.testclient import TestClient
import time
import os

import re

def test_speech2text_integration():
    app = create_app()

    with TestClient(app) as client:
        payload = {
            "url": "https://youtu.be/pVv7qGvhqvg?si=-DKS5_x_k7boAwjw",
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

# 유효하지 않은 URL로 인한 실패 코드 작성 필요
# def test_speech2text_integration_except():