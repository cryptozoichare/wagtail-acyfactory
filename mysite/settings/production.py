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
        "console": {
            "class": "logging.StreamHandler",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["console"],
            "level": os.getenv("DJANGO_LOG_LEVEL", "INFO"),
        },
    },
}

WAGTAIL_REDIRECTS_FILE_STORAGE = "cache"
STATIC_ROOT = "/home/public/static/"

try:
    from .local import *
except ImportError:
    pass