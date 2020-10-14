from datetime import datetime

from rest_framework.viewsets import ModelViewSet


class BaseDataModelViewSet(ModelViewSet):
    """
    数据模型视图集基类
    """
    def perform_create(self, serializer):
        """
        处理创建数据时，插入创建人和修改人
        :param serializer:
        :return:
        """
        kwargs = dict(creator_id=self.request.user.id, modifier_id=self.request.user.id)
        serializer.save(**kwargs)

    def perform_update(self, serializer):
        """
        处理修改数据时， 插入修改人
        :param serializer:
        :return:
        """
        kwargs = dict(modifier_id=self.request.user.id)
        serializer.save(**kwargs)

    def perform_destroy(self, instance):
        """
        处理删除数据时， 插入删除人、删除时间、删除标识
        :param instance:
        :return:
        """
        instance.deleter_id = self.request.user.id
        instance.delete_time = datetime.now()
        instance.is_del = True
        instance.modifier_id = self.request.user.id
        instance.save()
