from django.db import models

# Create your models here.
from django.db.models import DO_NOTHING, SET_NULL, CASCADE
from ..auth_user.models import User

from apps.models import NameNumberMixin, BaseDataModel
from utils.choices import gender_choices, id_type_choices, position_type_choices, position_status_choices, \
    entry_status_choices, entry_status_not_employed



class Employee(NameNumberMixin, BaseDataModel):
    """
    人员
    """
    user = models.OneToOneField(to=User, on_delete=SET_NULL, null=True, db_constraint=False)
    age = models.IntegerField(null=True)
    gender = models.IntegerField(null=True, choices=gender_choices)
    id_type = models.IntegerField(choices=id_type_choices, null=False, default=0)
    identity_card = models.CharField(max_length=len("441323199208260798"), null=False)
    mobile = models.CharField(max_length=len("15856858585"), null=False)

    photo = models.CharField(max_length=100, null=True)

    entry_status = models.PositiveIntegerField(choices=entry_status_choices, default=entry_status_not_employed)

    class Meta(object):
        db_table = "employee"
        indexes = [models.Index(fields=["user"]), models.Index(fields=["mobile"])]
