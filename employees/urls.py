from django.urls import path
from . import views
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
]
