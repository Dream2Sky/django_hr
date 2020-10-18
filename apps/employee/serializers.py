from datetime import datetime

from rest_framework import serializers, exceptions
from shortuuidfield import ShortUUIDField

from apps.employee.models import Employee, OrgUnit, OrgDepartment, Position, JobInformation
from apps.base.serializers import BaseHistoryModelSerializer


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name", "number", "age", "gender", "identity_card", "mobile", "user")


class OrganizationSerializer(BaseHistoryModelSerializer):
    begin_date = serializers.DateField(default=datetime.now().date(), allow_null=True)
    end_date = serializers.DateField(default=datetime(year=2199, month=12, day=31).date(), allow_null=True)
    parent = ShortUUIDField(blank=True, null=True)


class OrgUnitSerializer(OrganizationSerializer):
    class Meta:
        model = OrgUnit
        fields = ("id", "name", "number", "is_root", "begin_date", "end_date", "parent")


class OrgDepartmentSerializer(OrganizationSerializer):
    class Meta:
        model = OrgDepartment
        fields = ("id", "name", "number", "begin_date", "end_date", "parent", "unit")


class PositionSerializer(BaseHistoryModelSerializer):
    class Meta:
        model = Position
        fields = ("id", "name", "number", "begin_date", "end_date", "department")


class JobInformationSerializer(BaseHistoryModelSerializer):

    def validate(self, attrs):
        attrs = super(JobInformationSerializer, self).validate(attrs)
        position = attrs.get("position")
        department = attrs.get("department")
        unit = attrs.get("unit")

        if position.department == department and department.unit == unit:
            return attrs

        raise serializers.ValidationError("组织所属有误")

    class Meta:
        model = JobInformation
        fields = ("id", "employee", "position", "department", "unit", "position_type", "position_status", "begin_date",
                  "end_date")
