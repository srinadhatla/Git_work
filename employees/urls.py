from .views import EmployeeViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(
    "employees",
    EmployeeViewSet
)
urlpatterns = router.urls