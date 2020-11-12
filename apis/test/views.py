from rest_framework import status
from rest_framework.response import Response
from django_hr.libs.open_api import open_api
from apis.views import OpenAPIView


class TestView(OpenAPIView):
    """
    docstring
    """
    @open_api(name="test.get")
    def get(self, request, *args, **kwargs):

        return Response(data={"name": "heheh"}, status=status.HTTP_200_OK)


class Test2View(OpenAPIView):

    def get(self, request, *args, **kwargs):
        return Response(data={"name": "heheh"}, status=status.HTTP_200_OK)
