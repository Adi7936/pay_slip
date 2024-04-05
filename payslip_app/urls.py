from django.urls import path, include
from rest_framework import routers
from payslip_app.views import *

router = routers.DefaultRouter()
router.register(r'employees', EmployeeViewSet)
# router.register(r'payslips', PayslipViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('payslip/<int:pk>/download/', EmployeeViewSet.as_view({'get': 'download_payslip'}), name='download_payslip'),
]
