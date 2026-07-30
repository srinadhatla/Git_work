from rest_framework.routers import DefaultRouter
from .views import LeaveRequestViewSet

router = DefaultRouter()

router.register("leaves",LeaveRequestViewSet)
urlpatterns = router.urls