import os
import random
import string

from .base import *

DEBUG = False


SECRET_KEY = os.environ["SECRET_KEY"]

SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

SECURE_SSL_REDIRECT = True

ALLOWED_HOSTS = os.getenv("DJANGO_ALLOWED_HOSTS", "*").split(",")

CSRF_TRUSTED_ORIGINS = ["https://acyfactory.com", "https://acyfactory.nfshost.com"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "file": {
            "level": "DEBUG",
            "class": "logging.FileHandler",
            "filename": "/home/logs/django.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "DEBUG",
            "propagate": True,
        },
    },
}


WAGTAILDOCS_SERVE_METHOD = 'direct'

STATIC_ROOT = "/home/public/static/"
MEDIA_ROOT = "/home/public/media/"

try:
    from .local import *
except ImportError:
    pass