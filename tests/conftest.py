import pytest
from fastapi.testclient import TestClient

from app.main import create_app
from app.database.conn import db
