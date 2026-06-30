from django.urls import path
from . import views

from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet

urlpatterns = [
    path("",views.index, name='index'),
    path("home/",views.home, name="home"),
    path("about/",views.about, name='about'),
    path("contact/",views.contact, name='Contact'),
    path("view_employee/", views.employee_list, name="employee_list"),
    path("add/", views.add_employee, name="add_employee"),
    path("update/<int:id>/", views.update_employee, name="employee_update"),
    path("delete/<int:id>/", views.delete_employee, name="delete_employee"),
    path("filter/<int:id>/",views.filter_employee,name='filter_employee'),
    path('api/employees/',views.employee_list,name='employee_list_api'),
    path('api/employees/',views.employee_list_api),
    path('api/employees/<int:id>/',views.employee_detail_api),
    path('api/employees/create/',views.employee_create_api),
    path('api/employees/update/<int:id>/',views.employee_update_api),
    path('api/employees/delete/<int:id>/',views.employee_delete_api),
    path('api/cbv/employees/',views.EmployeeAPIView.as_view()),
    path('api/generic/employees/',views.EmployeeListAPIView.as_view(),),
    path('api/generic/employees/<int:pk>/',views.EmployeeRetrieveAPIView.as_view(),),
    path('api/generic/employees/create/',views.EmployeeCreateAPIView.as_view(),),
    path('api/generic/employees/update/<int:pk>/',views.EmployeeUpdateAPIView.as_view(),),
    path('api/generic/employees/delete/<int:pk>/',views.EmployeeDeleteAPIView.as_view(),),
    path("department-report/",views.department_report,name="department_report",),
]


router = DefaultRouter()

router.register(
    'employees',
    EmployeeViewSet,
    basename='employee'
)

urlpatterns += router.urls