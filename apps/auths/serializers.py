from rest_framework import serializers

from apps.auths.models import User
from apps.employee.models import Employee


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "number", "mobile")


class UserSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer()

    class Meta:
        model = User
        fields = ("id", "username", "employee")
