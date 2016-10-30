from .base import *

DEBUG = True


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'food_step',
        'USER': 'food_step',
        'PASSWORD': 'food_step',
        'HOST': 'localhost',
        'PORT': ''
    }
}
