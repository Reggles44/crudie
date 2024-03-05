import os
import dj_database_url
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-+q5@6v(@4xcp+3$e2)xggdd5p7z39!jk0j^xcov!p2+ei=3%go"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = [
    "crudie",
    "rest_framework",
    "django.contrib.contenttypes",
    "django.contrib.auth",
]
ROOT_URLCONF = "crudie.urls"
TEMPLATES = []
WSGI_APPLICATION = "crudie.wsgi.application"


# Database
DATABASES = {"default": dj_database_url.config(default=os.getenv("DATABASE_URL"))}


# Internationalization
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = "static/"

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
