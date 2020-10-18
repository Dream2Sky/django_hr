from rest_framework.views import APIView

from apps.attend.models import PunchRecord
from apps.attend.serializers import PunchRecordSerializer
from apps.base.views import BaseDataModelViewSet
from apps.employee.models import JobInformation


class PunchRecordViewSets(BaseDataModelViewSet):
    queryset = PunchRecord.objects.all()
    serializer_class = PunchRecordSerializer
