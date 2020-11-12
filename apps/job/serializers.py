from datetime import datetime

from rest_framework import serializers, exceptions
from shortuuidfield import ShortUUIDField

from apps.serializers import BaseHistoryModelSerializer
from .models import JobInformation


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
