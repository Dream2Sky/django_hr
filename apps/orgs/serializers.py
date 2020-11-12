from datetime import datetime

from rest_framework import serializers, exceptions
from shortuuidfield import ShortUUIDField

from apps.serializers import BaseHistoryModelSerializer
from .models import OrgUnit, OrgDepartment, Organization, Position


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
