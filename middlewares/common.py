import asyncio

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from django.http.response import JsonResponse
import json
# import logger
# import traceback


class OpenAPIResponseMiddleware(MiddlewareMixin):

    def process_response(self, request, response):
        
        if hasattr(response, "data"):
            response.data = {
                'code': 10000,
                'data': response.data,
                'msg': 'OK'
            }
            response._is_rendered = False
            response.render()

        return response

    def process_exception(self, request, exc):

        ret_json = {
            'code': exc.__class__.__name__,
            'msg': getattr(exc, 'message', 'error'),
            'data': None
        }
        response = JsonResponse(ret_json)
        response.status_code = getattr(exc, 'status_code', 500)

        return response
