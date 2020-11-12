import inspect


from rest_framework.decorators import api_view

class OpenApiDecorate:

    def __init__(self, name=None, is_login=False, version="v1"):
        self.name = name,
        self.version = version
        self.is_login = is_login

    def __call__(self, original_func):

        def _api_func(s1, *arg, **kwargs):
            if self.is_login and hasattr(s1, "request"):
                if hasattr(s1.request, "authenticators"):
                    s1.request.authenticators = []
            return original_func(s1, *arg, **kwargs)

        _doc = inspect.getdoc(original_func)
        _description = _doc.split("\n")[0] if _doc else ""
        _api_func.__api_name__ = self.name[0]
        _api_func.__origin_module_name__ = original_func.__module__
        _api_func.__api_origin_name__ = original_func.__name__
        _api_func.__api_description__ = _description
        _api_func.__api_doc__ = _doc
        _api_func.__api_path__ = f'api/{self.version}{_api_func.__origin_module_name__.replace(".", "/").replace("apis", "").replace("/views", "")}/{_api_func.__api_name__}'

        return _api_func

open_api = OpenApiDecorate