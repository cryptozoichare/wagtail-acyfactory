from .base import *
from dotenv import load_dotenv
load_dotenv()
import os


DEBUG = False

# Raises Django's ImproperlyConfigured
# exception if SECRET_KEY not in os.environ
SECRET_KEY = os.environ.get("SECRET_KEY")

ALLOWED_HOSTS = [".acyfactory.com", "acyfactory.nfshost.com"]

SESSION_COOKIE_SECURE = True

SERVER_EMAIL = "root@acyfactory.com"
DEFAULT_FROM_EMAIL = "webmaster@acyfactory.com"