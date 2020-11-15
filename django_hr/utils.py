import inspect
from django.urls import re_path, path, include
# from rest_framework.documentation import include_docs_urls
#
# from django_hr.routers import router
import importlib
import pkgutil


def iter_services(path=None, modules=list()):
    if isinstance(path, str):
        path = [path]

    for p in pkgutil.iter_modules(path=path):
        module_name = f"{path[0]}{p.name}"
        if p.ispkg:
            iter_services(path=[f"{module_name}/"], modules=modules)
            continue

        modules.append(module_name)


def service_loader(modules, loader_class):
    paths = list()
    _paths = dict()
    for module_path in modules:
        module_path = module_path.replace("../", "")
        module_path = module_path.replace("/", ".")
        module = importlib.import_module(module_path)

        for _name, _cls in inspect.getmembers(module, inspect.isclass):
            if inspect.getmodule(_cls) == module and issubclass(_cls, loader_class):
                if getattr(_cls, "api_resolve"):
                    _paths.update(_cls.api_resolve())

    for k, v in _paths.items():
        paths.append(v)

    return paths


def models_loader(modules, loader_class):
    model_dict = dict()
    for module_path in modules:
        module_path = module_path.replace("../", "")
        module_path = module_path.replace("/", ".")
        module = importlib.import_module(module_path)

        for _name, _cls in inspect.getmembers(module, inspect.isclass):
            if inspect.getmodule(_cls) == module and issubclass(_cls, loader_class):
                model_dict[_name] = _cls

    return model_dict
