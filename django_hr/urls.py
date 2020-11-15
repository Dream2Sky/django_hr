"""django_hr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
import inspect
from django.urls import re_path, path, include
# from rest_framework.documentation import include_docs_urls
#
# from django_hr.routers import router
import importlib
import pkgutil

from apis.views import OpenAPIView
import django_hr.utils as sys_utils


modules = list()
sys_utils.iter_services("apis/", modules=modules)

urlpatterns = sys_utils.service_loader(modules, OpenAPIView)

# def service_loader():
#     _paths = dict()
#     for module_path in modules:
#         module_path = module_path.replace("../", "")
#         module_path = module_path.replace("/", ".")
#         module = importlib.import_module(module_path)

#         for _name, _cls in inspect.getmembers(module, inspect.isclass):
#             if inspect.getmodule(_cls) == module and issubclass(_cls, OpenAPIView):
#                 if getattr(_cls, "api_resolve"):
#                     _paths.update(_cls.api_resolve())

#     for k, v in _paths.items():
#         paths.append(v)


# iter_services("apis/")
# service_loader()
# urlpatterns = paths
