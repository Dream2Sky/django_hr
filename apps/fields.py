from shortuuidfield import ShortUUIDField
from django.db import models


class LowerCaseShortUUIDField(ShortUUIDField):
    """
    小写 short uuid
    """

    def pre_save(self, model_instance, add):
        value = super(LowerCaseShortUUIDField, self).pre_save(
            model_instance, add)

        return value.lower()


class ForeignKeyWithOutDBConstraint(models.ForeignKey):

    def __init__(self, *args, **kwargs):
        kwargs.update({"db_constraint": False})
        super().__init__(*args, **kwargs)
