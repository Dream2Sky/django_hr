"""
ASGI config for django_hr project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

profile = os.environ.get("PROJECT_PROFILE", "dev")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_hr.settings.%s' % profile)

application = get_asgi_application()
