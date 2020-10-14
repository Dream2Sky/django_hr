from datetime import datetime

from rest_framework import serializers


class AuditSerializer(serializers.ModelSerializer):

    def save(self, **kwargs):
        if kwargs is None:
            kwargs = dict()
        request = self.context["request"]
        if request.method == "POST":
            kwargs["creator_id"] = request.user.id
            kwargs["modifier_id"] = request.user.id
        elif request.method in ["PUT", "PATCH"]:
            kwargs["modifier_id"] = request.user.id
        elif request.method == "DELETE":
            kwargs["is_del"] = True
            kwargs["delete_time"] = datetime.now()
            kwargs["deleter_id"] = request.user.id
        super(AuditSerializer, self).save(**kwargs)

