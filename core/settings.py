# from decouple import config, Csv
# from pathlib import Path, os
# from django.contrib.messages import constants as messages


# BASE_DIR = Path(__file__).resolve().parent.parent

# SECRET_KEY = config("SECRET_KEY")

# DEBUG = config("DEBUG", default=False, cast=bool)

# DOMAIN = 'https://8000-idx-cms-1716871489073.cluster-bs35cdu5w5cuaxdfch3hqqt7zm.cloudworkstations.dev'

# ALLOWED_HOSTS = [DOMAIN, '127.0.0.1', 'localhost']

# CSRF_TRUSTED_ORIGINS = [DOMAIN, 'http://127.0.0.1', 'http://localhost']

# # ALLOWED_HOSTS = config('ALLOWED_HOSTS', cast=Csv())

# # CSRF_TRUSTED_ORIGINS = config('CSRF_TRUSTED_ORIGINS', cast=list)

# SECURE_BROWSER_XSS_FILTER = config("SECURE_BROWSER_XSS_FILTER", cast=bool)
# SECURE_CONTENT_TYPE_NOSNIFF = config("SECURE_CONTENT_TYPE_NOSNIFF", cast=bool)

# SECURE_SSL_REDIRECT = config("SECURE_SSL_REDIRECT", default=False, cast=bool)
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# SECURE_HSTS_SECONDS = config("SECURE_HSTS_SECONDS")
# SECURE_HSTS_PRELOAD = config("SECURE_HSTS_PRELOAD", cast=bool)
# SECURE_HSTS_INCLUDE_SUBDOMAINS = config("SECURE_HSTS_INCLUDE_SUBDOMAINS", cast=bool)

# SESSION_COOKIE_SECURE = config("SESSION_COOKIE_SECURE", cast=bool)
# CSRF_COOKIE_SECURE = config("CSRF_COOKIE_SECURE", cast=bool)

# INSTALLED_APPS = [
#     'django.contrib.admin',
#     'django.contrib.auth',
#     'django.contrib.contenttypes',
#     'django.contrib.sessions',
#     'django.contrib.messages',
#     'django.contrib.staticfiles',
#     # 'compressor',
#     'django_htmx',
#     'account',
#     'cms',
# ]

# MIDDLEWARE = [
#     'django.middleware.cache.UpdateCacheMiddleware',
#     'django.middleware.security.SecurityMiddleware',
#     'django.contrib.sessions.middleware.SessionMiddleware',
#     'django.middleware.gzip.GZipMiddleware',
#     'django.middleware.common.CommonMiddleware',
#     'django.middleware.csrf.CsrfViewMiddleware',
#     'django.contrib.auth.middleware.AuthenticationMiddleware',
#     'django.contrib.messages.middleware.MessageMiddleware',
#     'django.middleware.clickjacking.XFrameOptionsMiddleware',
#     'django_htmx.middleware.HtmxMiddleware',
#     'django.middleware.cache.FetchFromCacheMiddleware',
# ]

# ROOT_URLCONF = 'core.urls'

# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],
#         'APP_DIRS': True,
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#             ],
#         },
#     },
# ]

# WSGI_APPLICATION = 'core.wsgi.application'

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'NAME': config("DB_NAME"),
#         'USER': config("DB_USER"),
#         'PASSWORD': config("DB_PASSWORD"),
#         'HOST': config("DB_HOST"),
#         'PORT': config("DB_POPRT")
#     }
# }

# AUTH_PASSWORD_VALIDATORS = [
#     {
#         'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
#     },
#     {
#         'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
#     },
# ]

# LANGUAGE_CODE = 'en-us'
# TIME_ZONE = 'UTC'
# USE_I18N = True
# USE_TZ = True

# STATIC_URL = 'static/'
# STATIC_ROOT = os.path.join(BASE_DIR ,'static')
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static_src')]

# MEDIA_URL = 'media/'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# # STATIC_URL = "static/"   
# # MEDIA_URL = "media/"    

# # STATIC_ROOT = "/vol/static"
# # MEDIA_ROOT = "/vol/media"

# # STATICFILES_FINDERS = (
# #     'django.contrib.staticfiles.finders.FileSystemFinder',
# #     'django.contrib.staticfiles.finders.AppDirectoriesFinder',
# #     'compressor.finders.CompressorFinder',
# # )

# # COMPRESS_ENABLED = True
# # COMPRESS_ROOT = STATIC_ROOT
# # COMPRESS_OFFLINE = True

# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# EMAIL_HOST = config("EMAIL_HOST")
# EMAIL_PORT = config("EMAIL_PORT")
# EMAIL_USE_TLS = config("EMAIL_USE_TLS")
# EMAIL_HOST_USER = config("EMAIL_HOST_USER")
# EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")

# MESSAGE_LEVEL = 10

# MESSAGE_TAGS = {
#     messages.INFO: 'is-info',
#     messages.SUCCESS: 'is-primary',
#     messages.WARNING: 'is-warning',
#     messages.ERROR: 'is-danger',
# }

# DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# # CACHES = {
# #     "default": {
# #         "BACKEND": "django.core.cache.backends.redis.RedisCache",
# #         "LOCATION": config("CACHE_LOCATION"),
# #         "OPTIONS": {
# #             "pool_class": "redis.BlockingConnectionPool",
# #         },
# #         "KEY_PREFIX": "cms_cache",
# #     }
# # }
# # CACHE_MIDDLEWARE_ALIAS = 'default'
# # CACHE_MIDDLEWARE_SECONDS = 900