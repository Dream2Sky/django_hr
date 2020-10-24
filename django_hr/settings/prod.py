from .base import *

DEBUG = True
ALLOWED_HOSTS = ["150.109.247.43", ]

DB_USER = 'root'
DB_PORT = '3306'
DB_PASSWORD = 'Root)f3=!.732'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': DB_NAME,
        'HOST': 'localhost',
        'PORT': DB_PORT,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD
    }
}