from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING, SET_NULL, CASCADE
from ..auth_user.models import User

from apps.models import NameNumberMixin, BaseDataHistoryModel
from apps.fields import ForeignKeyWithOutDBConstraint
from ..emp.models import Employee
from utils.choices import gender_choices, id_type_choices, position_type_choices, position_status_choices, \
    entry_status_choices, entry_status_not_employed


class Organization(NameNumberMixin, BaseDataHistoryModel):
    """
    组织类型基类
    """
    parent = ForeignKeyWithOutDBConstraint("self", on_delete=CASCADE, null=True)

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
    unit = ForeignKeyWithOutDBConstraint(OrgUnit, on_delete=CASCADE, null=True)

    class Meta(object):
        db_table = "org_department"


class Position(NameNumberMixin, BaseDataHistoryModel):
    """
    岗位
    """
    department = ForeignKeyWithOutDBConstraint(OrgDepartment, on_delete=CASCADE)

    class Meta(object):
        db_table = "position"
