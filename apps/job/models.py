from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING, SET_NULL, CASCADE

from apps.models import NameNumberMixin, BaseDataHistoryModel
from apps.fields import ForeignKeyWithOutDBConstraint
from ..emp.models import Employee
from utils.choices import gender_choices, id_type_choices, position_type_choices, position_status_choices, \
    entry_status_choices, entry_status_not_employed
from ..orgs.models import Position, OrgDepartment, OrgUnit


class JobInformation(BaseDataHistoryModel):
    """
    任职
    """
    employee = ForeignKeyWithOutDBConstraint(Employee, on_delete=CASCADE)
    position = ForeignKeyWithOutDBConstraint(Position, on_delete=CASCADE)
    department = ForeignKeyWithOutDBConstraint(OrgDepartment, on_delete=CASCADE)
    unit = ForeignKeyWithOutDBConstraint(OrgUnit, on_delete=CASCADE)

    position_type = models.IntegerField(choices=position_type_choices)
    position_status = models.IntegerField(choices=position_status_choices)

    class Meta(object):
        db_table = "jobinformation"
