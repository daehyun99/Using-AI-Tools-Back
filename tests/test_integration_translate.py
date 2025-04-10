import pytest

from app.main import create_app
from fastapi.testclient import TestClient

from app.common.config import test_receiver

import time
import os
import re


@pytest.mark.parametrize("service_name", ["deepl", "openai"])
def test_translate_integration(service_name):
    app = create_app()

    with TestClient(app) as client:
        test_file_path = os.path.join("tests", "example.pdf")
        receiver_email = test_receiver

        with open(test_file_path, "rb") as f:
            files = {
                "file": ("example.pdf", f, "application/pdf")
            }
            data = {
                "service": service_name,
                "email_address": receiver_email
            }
            response = client.post(f"/Translate/?service={service_name}", files=files, data=data)

        assert response.status_code == 200
        json_data = response.json()


        assert "status" in json_data or "message" in json_data
        assert json_data.get("status", "success").lower() in ["success", "ok"]


def test_translate_integration_except():
    app = create_app()

    with TestClient(app) as client:
        ...