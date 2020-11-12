from django.db import models
from django.db.models import CASCADE

from apps.models import BaseDataModel
from apps.fields import ForeignKeyWithOutDBConstraint
from ..emp.models import Employee
from ..orgs.models import OrgDepartment


class PunchRecord(BaseDataModel):
    """
    打卡表
    """
    employee = ForeignKeyWithOutDBConstraint(
        Employee, on_delete=CASCADE, db_index=True)
    department = ForeignKeyWithOutDBConstraint(
        OrgDepartment, on_delete=CASCADE, db_index=True)
    punch_time = models.DateTimeField(db_index=True)
    punch_point = models.CharField(max_length=100, null=True)
    description = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = "punch_record"
        indexes = [
            models.Index(fields=['employee', 'punch_time']),
            models.Index(fields=['department', 'punch_time']),
        ]
