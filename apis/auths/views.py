from rest_framework_jwt.views import ObtainJSONWebToken
from rest_framework_jwt.serializers import JSONWebTokenSerializer

from django_hr.libs.open_api import open_api
from apis.views import OpenAPIView
from apps.auth_user.serializers import UserSerializer


class JWTAuthsAPIView(OpenAPIView, ObtainJSONWebToken):

    @open_api(name="login")
    def login(self, request, *args, **kwargs):
        return super(JWTAuthsAPIView, self).post(request, *args, **kwargs)
