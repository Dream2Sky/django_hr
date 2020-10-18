from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from apps.auths.models import User
from apps.base.views import BaseDataModelViewSet
from apps.employee.models import Employee, OrgUnit, OrgDepartment, Position, JobInformation
from apps.employee.serializers import EmployeeSerializer, OrgUnitSerializer, OrgDepartmentSerializer, \
    PositionSerializer, JobInformationSerializer
from apps.utils import auth
from apps.utils.employee import entry_status_employed


class EmployeeViewSets(BaseDataModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class OrgUnitViewSets(BaseDataModelViewSet):
    queryset = OrgUnit.objects.all()
    serializer_class = OrgUnitSerializer

    def perform_create(self, serializer):
        is_root = serializer.validated_data.get("is_root")
        parent = serializer.validated_data.get("parent")
        if is_root:
            root_units = self.queryset.filter(is_root=is_root).all()
            if len(root_units) > 0:
                raise ValidationError("根组织只能有一个")
            if parent:
                raise ValidationError("根组织不应该有父级组织")
        elif not parent:
            raise ValidationError("非根组织需要有父级组织")

        super(OrgUnitViewSets, self).perform_create(serializer)


class OrgDepartmentViewSets(BaseDataModelViewSet):
    queryset = OrgDepartment.objects.all()
    serializer_class = OrgDepartmentSerializer

    @staticmethod
    def validate_org_unit_uniformity(unit, parent_depart):
        """
        校验当前部门所属单位是否和父级部门的所属单位是否一致
        :param unit:
        :param parent_depart:
        :return:
        """
        if parent_depart:
            parent_unit = parent_depart.get("unit", {})
            if parent_unit.get("id") != unit.get("id"):
                raise ValidationError("所属单位必须和父级部门所属单位一致")

        return True

    def perform_create(self, serializer):
        unit = serializer.validated_data.get("unit")
        parent = serializer.validated_data.get("parent")
        self.validate_org_unit_uniformity(unit, parent)
        super(OrgDepartmentViewSets, self).perform_create(serializer)

    def perform_update(self, serializer):
        unit = serializer.validated_data.get("unit")
        parent = serializer.validated_data.get("parent")
        self.validate_org_unit_uniformity(unit, parent)
        super(OrgDepartmentViewSets, self).perform_update(serializer)


class PositionViewSets(BaseDataModelViewSet):
    queryset = Position.objects.all()
    serializer_class = PositionSerializer


class JobInformationViewSets(BaseDataModelViewSet):
    queryset = JobInformation.objects.all()
    serializer_class = JobInformationSerializer

    def perform_create(self, serializer):
        from django.db import transaction

        with transaction.atomic():
            employee = serializer.validated_data.get("employee")
            employee.entry_status = entry_status_employed

            user = User.objects.create_user(username=employee.mobile, password=auth.generate_random_password())
            employee.user = user

            employee.save()

            super(JobInformationViewSets, self).perform_create(serializer)

    def destroy(self, request, *args, **kwargs):
        raise Http404()
