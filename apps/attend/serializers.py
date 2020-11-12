import datetime

from django.conf import settings
from pytz import timezone
from rest_framework import serializers
from shortuuid import ShortUUID

from ..emp.models import Employee
from ..job.models import JobInformation
from .models import PunchRecord


class PunchRecordSerializer(serializers.ModelSerializer):
    employee = serializers.CharField(required=False)
    department = serializers.CharField(required=False)
    punch_time = serializers.DateTimeField(required=False)

    def validate(self, attrs):
        attrs = super(PunchRecordSerializer, self).validate(attrs)
        punch_time = attrs.get("punch_time")
        if punch_time:
            end_time = datetime.datetime.strptime(datetime.datetime.now().date().strftime("%Y-%m-%d") + " 23:59:59",
                                                  "%Y-%m-%d %H:%M:%S").replace(tzinfo=timezone(settings.TIME_ZONE))
            if punch_time > end_time:
                raise serializers.ValidationError("无效的打卡时间")
        else:
            punch_time = datetime.datetime.now().replace(
                tzinfo=timezone(settings.TIME_ZONE))

        employee = attrs.get("employee")
        if not employee:
            employee = self.context["request"].user.employee
        else:
            employee = Employee.objects.filter(pk=employee).first()

        job = JobInformation.objects.filter(employee=employee).first()
        attrs["employee"] = employee
        attrs["department"] = job.department
        attrs["punch_time"] = punch_time

        return attrs

    class Meta:
        model = PunchRecord
        fields = ("id", "employee", "punch_time", "department")
