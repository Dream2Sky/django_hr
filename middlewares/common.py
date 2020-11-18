import asyncio

from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from django.http.response import JsonResponse
import json
import logging
import traceback
import threading
# Exception

local = threading.local()


class ErrorLogFilter(logging.Filter):
    """
    日志过滤器
    """

    def filter(self, record):
        record.path = getattr(local, 'path', 'none')
        record.method = getattr(local, 'method', 'none')
        record.track_info = getattr(local, 'track_info', 'none')

        return True


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

        local.path = request.path
        local.method = request.method
        local.track_info = traceback.format_exc()

        logger = logging.getLogger("error.log")
        logger.error(msg="message", exc_info=exc, stack_info=True)

        ret_json = {
            'code': exc.__class__.__name__,
            'msg': getattr(exc, 'msg', 'error'),
            'data': None
        }
        response = JsonResponse(ret_json)
        response.status_code = getattr(exc, 'status_code', 500)

        return response
