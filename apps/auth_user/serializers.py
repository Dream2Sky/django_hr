from rest_framework import serializers

from .models import User
from ..emp.serializers import EmployeeSerializer


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "employee")


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'auth_user': UserSerializer(user, context={'request': request}).data
    }
