"""
WSGI config for django_hr project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django_hr.environment import environment

profile = os.environ.get("PROJECT_PROFILE", "dev")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_hr.settings.%s' % profile)

application = get_wsgi_application()
