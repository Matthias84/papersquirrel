from .base import *


DEBUG = False

SECRET_KEY = '' # enter a long random string

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'de-de'

TIME_ZONE = 'Europe/Berlin'
