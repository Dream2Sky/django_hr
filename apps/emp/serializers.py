from datetime import datetime

from rest_framework import serializers, exceptions
from shortuuidfield import ShortUUIDField

from .models import Employee
from apps.serializers import BaseHistoryModelSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "number", "age", "gender", "identity_card", "mobile", "auth_user")
