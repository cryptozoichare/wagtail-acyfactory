from .base import *
import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


DEBUG = False

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [".acyfactory.com", "acyfactory.nfshost.com"]

SECURE_SSL_REDIRECT = True
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

SERVER_EMAIL = "root@acyfactory.com"
DEFAULT_FROM_EMAIL = "webmaster@acyfactory.com"