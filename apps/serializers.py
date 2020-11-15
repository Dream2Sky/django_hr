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


class CommonModelSerializer(serializers.Serializer):
    model = serializers.CharField(
        required=True, error_messages={"required": "invalid model name"})


class CommonModelListSerializer(CommonModelSerializer):
    filter_dict = serializers.JSONField(
        required=True, error_messages={"required": "invalid filter_dict"})
    page_index = serializers.IntegerField(default=1)
    page_size = serializers.IntegerField(default=20)


class CommonModelGetSerializer(CommonModelSerializer):
    id_ = serializers.IntegerField(required=True)


class CommonModelCreateSerializer(CommonModelSerializer):
    info = serializers.JSONField(
        required=True, error_messages={"required": "invalid info"})


class CommonModelEditSerializer(CommonModelGetSerializer, CommonModelCreateSerializer):
    pass
