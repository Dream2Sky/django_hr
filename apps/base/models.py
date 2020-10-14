from django.db import models

from apps.utils.audit.models import AuditMixin, FakeDelMixin
from shortuuidfield import ShortUUIDField


class BaseDataModelManager(models.Manager):
    """
    重写BaseDataModel的Manager， 过滤掉标记掉删除的数据
    """

    def get_queryset(self):
        return super(BaseDataModelManager, self).get_queryset().filter(is_del=False).all()


class NameNumberMixin(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    number = models.CharField(max_length=100, null=True, blank=True, unique=True)

    class Meta(object):
        abstract = True


class BaseModel(AuditMixin):
    id = ShortUUIDField(primary_key=True)

    class Meta(object):
        abstract = True


class BaseDataModel(FakeDelMixin, BaseModel):
    objects = BaseDataModelManager()
    full_objects = models.Manager()

    class Meta(object):
        abstract = True


class BaseDataHistoryModel(BaseDataModel):
    begin_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

    class Meta(object):
        abstract = True
