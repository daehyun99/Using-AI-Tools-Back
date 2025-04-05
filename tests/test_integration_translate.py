from app.main import create_app
from fastapi.testclient import TestClient

import time
import os
import re


def test_translate_integration():
    app = create_app()

    with TestClient(app) as client:
        ...


def test_translate_integration_except():
    app = create_app()

    with TestClient(app) as client:
        ...