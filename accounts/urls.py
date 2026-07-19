from django.urls import path
from .views import LoginAPIView, RefreshTokenAPIView, LogoutAPIView, ChangePasswordAPIView, ForgotPasswordAPIView, UserProfileAPIView, RestPasswordAPIView


urlpatterns = [
    path("login/",LoginAPIView.as_view(),name="Login"),
    path("refresh/",RefreshTokenAPIView.as_view(),name="refresh"),
    path("logout/",LogoutAPIView.as_view(),name="logout"),
    path("change-password/",ChangePasswordAPIView.as_view(),name="change-password"),
    path("forgot-password/",ForgotPasswordAPIView.as_view(),name="forgot-password"),
    path("reset-password/",RestPasswordAPIView.as_view(),name="reset-password"),
    path("profile/",UserProfileAPIView.as_view(),name="profile"),
]

