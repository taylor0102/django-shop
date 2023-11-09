from .base import *


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': os.environ.get('DATABASE-NAME', 'store'),
#         'USER': os.environ.get('DATABASE-USER', 'store'),
#         'PASSWORD': os.environ.get('DATABASE-PASSWORD', 'uhbgrtgdvcgyrrjb746462299477.012#$%^jfbjf'),
#         'HOST': os.environ.get('DATABASE-HOST', '127.0.0.1'),
#         'PORT': os.environ.get('DATABASE-PORT', 5432)
#     }}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
