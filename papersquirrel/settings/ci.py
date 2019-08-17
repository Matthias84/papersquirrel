from .base import *

# Setup for Travis CI and test coverage via coveralls

DEBUG = True

SECRET_KEY = 'cy098Cy4563057w2._:,73E3kpsa9=9§J§(J§()$§H/ncx,my'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
    }
}

LANGUAGE_CODE = 'en-en'

TIME_ZONE = 'Europe/Berlin'
