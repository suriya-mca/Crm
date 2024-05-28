from decouple import config
from .base import *

DEBUG = config("DEBUG", default=False, cast=bool)

DOMAIN = 'https://8000-idx-cms-1716871489073.cluster-bs35cdu5w5cuaxdfch3hqqt7zm.cloudworkstations.dev'

ALLOWED_HOSTS = [DOMAIN, '127.0.0.1', 'localhost', "*"]

CSRF_TRUSTED_ORIGINS = [DOMAIN, 'http://127.0.0.1', 'http://localhost']