from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response


class BaseResultMiddleWare(MiddlewareMixin):

    def process_response(self, request, response):
        return Response(dict(code=200, msg="", data=response.data))

