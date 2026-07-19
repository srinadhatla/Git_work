from django.urls import path
from . import views
from .views import DocumentUploadAPIView, DocumentListAPIView, DocumentDownloadAPIView, DocumentDeleteAPIView, EmployeeExcelImportAPIView, EmployeeExcelExportAPIView, EmployeeCSVImportAPIView, EmployeeCSVExportAPIView, EmployeeProfilePDFAPIView

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

router = DefaultRouter()
router.register(r"api/employees", EmployeeViewSet, basename="employee")

urlpatterns = [
    path("",views.dashboard, name="dashboard"),
    path("employees/", views.employee_list, name="employee_list"),
    path("departments/", views.department_list, name="department_list"),
    path("employees/search/", views.employee_search, name="employee_search"),
    path("documents/upload/",DocumentUploadAPIView.as_view()),
    path("documents/",DocumentListAPIView.as_view()),
    path("documents/<int:id>/download/",DocumentDownloadAPIView.as_view()),
    path("documents/<int:id>/delete/",DocumentDeleteAPIView.as_view()),
    path('employees/import/',EmployeeExcelImportAPIView.as_view()),
    path('employees/export/',EmployeeExcelExportAPIView.as_view()),
    path('employees/csv/import/',EmployeeCSVImportAPIView.as_view()),
    path('employees/csv/export/',EmployeeCSVExportAPIView.as_view()),
    path('employees/<int:id>/profile-pdf/',EmployeeProfilePDFAPIView.as_view()),
]


urlpatterns += router.urls