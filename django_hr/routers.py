from rest_framework import routers

from apps.attend.views import PunchRecordViewSets
from apps.employee.views import EmployeeViewSets, OrgUnitViewSets, OrgDepartmentViewSets, PositionViewSets, JobInformationViewSets

router = routers.DefaultRouter()

router.register("employees", EmployeeViewSets)
router.register("org_unit", OrgUnitViewSets)
router.register("org_depart", OrgDepartmentViewSets)
router.register("position", PositionViewSets)
router.register("jobinformation", JobInformationViewSets)
router.register("punch_record", PunchRecordViewSets)