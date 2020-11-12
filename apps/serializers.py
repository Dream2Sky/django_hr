from rest_framework import serializers


class BaseHistoryModelSerializer(serializers.ModelSerializer):

    def validate(self, attrs):
        self.validate_time_line(attrs)

        return super(BaseHistoryModelSerializer, self).validate(attrs)

    def validate_time_line(self, attrs):
        begin_date = attrs.get("begin_date")
        end_date = attrs.get("begin_date")

        if begin_date > end_date:
            raise serializers.ValidationError("结束时间必须大于或等于开始时间")
