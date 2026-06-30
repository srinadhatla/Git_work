from django.urls import path
from . import views
from . views import CustomPasswordChangeView
from django.contrib.auth import views as auth_views

urlpatterns = [
    
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/',views.profile,name='profile'),
    path('add_employee/',views.add_employee, name='add_employee'),
    path('update_employee/',views.update_employee, name='update_employee'),
    path('delete_employee/',views.delete_employee, name='delete_employee'),
    path('view_reports/',views.view_reports, name='view_reports'),
    path('admin_dashboard/',views.admin_dashboard,name='admin_dashboard'),
    path('hr_dashboard/',views.hr_dashboard,name='hr_dashboard'),
    path('employee_dashboard/',views.employee_dashboard,name='employee_dashboard'),
    path('change_password/',CustomPasswordChangeView.as_view(), name='change_password'),
    path('forgot_password/',auth_views.PasswordResetView.as_view(template_name='accounts/forgot_password.html'),name='password_reset'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name = 'accounts/reset_password.html'), name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name='accounts/reset_complete.html'),name='password_reset_complete'),
    path('verify_email/<int:user_id>/',views.verify_email,name='verify_email'),
    path('update_profile/',views.update_profile,name='update_profile'),
]