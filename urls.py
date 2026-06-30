"""
URL configuration for company_portal project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.routers import DefaultRouter
from employees.views import EmployeeViewSet
from departments.views import DepartmentViewSet
from accounts.views import UserViewSet

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Employee Management API",
        default_version='v1',
        description="Employee Management System APIs",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls), 
    path("", include('employees.urls')),
    path('accounts/', include('accounts.urls')),
    path('api/login/',TokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('api/token/refresh/',TokenRefreshView.as_view(),name='token_refresh'),
    path('swagger/',schema_view.with_ui('swagger',cache_timeout=0),name='swagger'),
    path('redoc/',schema_view.with_ui('redoc',cache_timeout=0),name='redoc'),
    path('api/v1/', include('api.v1.urls')),
    path('api/v2/', include('api.v2.urls')),
]


urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

router = DefaultRouter()

router.register('employees',EmployeeViewSet)
router.register('departments',DepartmentViewSet)
router.register('users',UserViewSet)

urlpatterns += router.urls
