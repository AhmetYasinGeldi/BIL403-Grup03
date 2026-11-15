"""Uygulama ayarları. Gizli değerler koddan ayrı, ortam değişkenlerinden okunur."""
import os
from datetime import timedelta

from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    STAFF_INVITE_CODE = os.environ.get("STAFF_INVITE_CODE")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or None
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(
        minutes=int(os.environ.get("SESSION_TIMEOUT_MINUTES", "30"))
    )
    RETENTION_DAYS = int(os.environ.get("RETENTION_DAYS", "365"))


class TestConfig(Config):
    TESTING = True
    SECRET_KEY = "test-secret-key"
    STAFF_INVITE_CODE = "test-invite-code"
    SQLALCHEMY_DATABASE_URI = "sqlite:///:memory:"
