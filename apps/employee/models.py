from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING, SET_NULL, CASCADE

from apps.auths.models import User
from apps.base.models import BaseDataModel, BaseModel, BaseDataHistoryModel, NameNumberMixin
from apps.utils.employee import gender_choices, id_type_choices, position_type_choices, position_status_choices


class Employee(NameNumberMixin, BaseDataModel):
    """
    人员
    """
    user = models.OneToOneField(to=User, on_delete=SET_NULL, null=True)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(null=True, choices=gender_choices)
    id_type = models.IntegerField(choices=id_type_choices, null=False, default=0)
    identity_card = models.CharField(max_length=len("441323199208260798"), null=False)
    mobile = models.CharField(max_length=len("15856858585"), null=False)

    photo = models.CharField(max_length=100, null=True)

    class Meta(object):
        db_table = "employee"


class Organization(NameNumberMixin, BaseDataHistoryModel):
    """
    组织类型基类
    """
    parent = models.ForeignKey("self", on_delete=CASCADE, null=True)

    class Meta(object):
        abstract = True


class OrgUnit(Organization):
    """
    组织单位
    """
    is_root = models.BooleanField(default=False)

    class Meta(object):
        db_table = "org_unit"


class OrgDepartment(Organization):
    """
    组织部门
    """
    unit = models.ForeignKey(OrgUnit, on_delete=CASCADE, null=True)

    class Meta(object):
        db_table = "org_department"


class Position(NameNumberMixin, BaseDataHistoryModel):
    """
    岗位
    """
    department = models.ForeignKey(OrgDepartment, on_delete=CASCADE)

    class Meta(object):
        db_table = "position"


class JobInformation(BaseDataHistoryModel):
    """
    任职
    """
    employee = models.ForeignKey(Employee, on_delete=CASCADE)
    position = models.ForeignKey(Position, on_delete=CASCADE)
    department = models.ForeignKey(OrgDepartment, on_delete=CASCADE)
    unit = models.ForeignKey(OrgUnit, on_delete=CASCADE)

    position_type = models.IntegerField(choices=position_type_choices)
    position_status = models.IntegerField(choices=position_status_choices)

    class Meta(object):
        db_table = "jobinformation"
