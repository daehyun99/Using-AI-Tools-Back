import pytest

from app.main import create_app
from fastapi.testclient import TestClient

import time
import os
import re


@pytest.mark.parametrize("service_name", ["deepl", "openai"])
def test_translate_integration(service_name):
    app = create_app()

    with TestClient(app) as client:
        test_file_path = os.path.join("tests", "example.pdf")

        with open(test_file_path, "rb") as f:
            files = {
                "file": ("example.pdf", f, "application/pdf")
            }
            response = client.post(f"/Translate/?service={service_name}", files=files)

        assert response.status_code == 200
        assert "application/pdf" in response.headers["content-type"] or "application/octet-stream" in response.headers["content-type"]
        assert response.headers.get("content-disposition", "").startswith("attachment")


def test_translate_integration_except():
    app = create_app()

    with TestClient(app) as client:
        ...