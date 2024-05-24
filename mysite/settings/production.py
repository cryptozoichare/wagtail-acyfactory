import os

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
            "level": "WARNING",
            "class": "logging.FileHandler",
            "filename": "/home/logs/django.log",
        },
    },
    "loggers": {
        "django": {
            "handlers": ["file"],
            "level": "WARNING",
            "propagate": True,
        },
    },
}



STATIC_ROOT = "/home/public/static/"
MEDIA_ROOT = "/home/public/media/"

try:
    from .local import *
except ImportError:
    pass
