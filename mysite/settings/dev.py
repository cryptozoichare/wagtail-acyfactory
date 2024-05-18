from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)62yk@1&l2(hquq@o$#5*^liiwa6#b8j+v(kutl^1qduh&ju8y"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"




INTERNAL_IPS = [
    "127.0.0.1",
]


try:
    from .local import *
except ImportError:
    pass