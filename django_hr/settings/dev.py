from .base import *

DEBUG = True
ALLOWED_HOSTS = []

DB_NAME = 'django_hr'
DB_USER = 'root'
DB_PORT = '3306'
DB_PASSWORD = '888888'
print(DB_PASSWORD)
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
REST_FRAMEWORK.update({
    "DEFAULT_RENDERER_CLASSES": ('rest_framework.renderers.JSONRenderer',)
})
