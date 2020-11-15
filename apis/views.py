from rest_framework.views import APIView
from django.conf import settings
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

import inspect
from functools import update_wrapper

from apps.serializers import CommonModelCreateSerializer
import django_hr.environment as env
from django_hr.libs.open_api import open_api


class OpenAPIView(APIView):

    paths = dict()

    @classmethod
    def api_resolve(cls, **initkwargs):

        def view(request, *args, **kwargs):
            self = cls(**initkwargs)
            self.setup(request, *args, **kwargs)
            if not hasattr(self, 'request'):
                raise AttributeError(
                    "%s instance has no 'request' attribute. Did you override "
                    "setup() and forget to call super()?" % cls.__name__
                )
            return self.dispatch(request, *args, **kwargs)

        for _method_name, _method in inspect.getmembers(cls, inspect.isfunction):
            if hasattr(_method, "__api_name__"):
                view.view_class = cls
                view.view_initkwargs = initkwargs
                update_wrapper(view, cls, updated=())
                update_wrapper(view, cls.dispatch, assigned=())
                cls.paths[_method.__api_path__] = path(
                    _method.__api_path__, csrf_exempt(view))

        return cls.paths

    def dispatch(self, request, *args, **kwargs):
        """
        `.dispatch()` is pretty much the same as Django's regular dispatch,
        but with extra hooks for startup, finalize, and exception handling.
        """
        self.args = args
        self.kwargs = kwargs
        request = self.initialize_request(request, *args, **kwargs)
        self.request = request
        self.headers = self.default_response_headers  # deprecate?

        try:
            self.initial(request, *args, **kwargs)

            # Get the appropriate handler method
            handler = self.resolve(request)

            response = handler(request, *args, **kwargs)

        except Exception as exc:
            response = self.handle_exception(exc)

        self.response = self.finalize_response(
            request, response, *args, **kwargs)
        return self.response

    def resolve(self, request):
        path = request.path
        api_name = path.split("/")[-1]

        if not api_name:
            raise Exception("无法找到匹配的api信息")

        for _method_name, _method in inspect.getmembers(self.__class__, inspect.isfunction):
            if hasattr(_method, "__api_name__") and _method.__api_name__ == api_name:
                api = getattr(self, _method_name)
                break

        if not api:
            return self.http_method_not_allowed

        return api


class CURDBaseAPIView(OpenAPIView):

    @open_api(name="common.model.create")
    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = CommonModelCreateSerializer(data=data)
        if not serializer.is_valid():
            raise Exception(serializer.error_messages)

        model_name = serializer.validated_data.get("model")
        if model_name not in env.environment.model_dict:
            raise Exception("invalid model name")

        model_cls = env.environment.model_dict[model_name]
        result = model_cls.objects.create(
            **serializer.validated_data.get("info"))

        return {"id": result.id}
