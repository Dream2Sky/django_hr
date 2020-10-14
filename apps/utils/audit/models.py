from django.db import models


class AuditMixin(models.Model):
    """
    审计字段模型
    """

    class Meta(object):
        abstract = True

    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")
    creator_id = models.CharField(max_length=100, verbose_name="创建人")
    modify_time = models.DateTimeField(auto_now=True, verbose_name="修改时间")
    modifier_id = models.CharField(max_length=100, verbose_name="修改人")


class FakeDelMixin(models.Model):
    """
    软删除模型
    """

    class Meta(object):
        abstract = True

    is_del = models.BooleanField(verbose_name="是否删除", null=False, default=False)
    delete_time = models.DateTimeField(verbose_name="删除时间", null=True)
    deleter_id = models.CharField(max_length=100, verbose_name="删除人")
