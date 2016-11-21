import os
from .base import *

DEBUG = False
ALLOWED_HOSTS = ['*']


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get('FOODSTEP_DB_NAME'),
        'USER': os.environ.get('FOODSTEP_DB_USER'),
        'PASSWORD': os.environ.get('FOODSTEP_DB_PASSWORD'),
        'HOST': os.environ.get('FOODSTEP_DB_HOST'),
        'PORT': os.environ.get('FOODSTEP_DB_PORT')
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'file': {
            'level': 'WARNING',
            'class': 'logging.FileHandler',
            'filename': os.path.join(BASE_DIR, 'django.log'),
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'WARNING',
            'propagate': True,
        },
    },
}
