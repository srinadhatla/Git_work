from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .serializers import LoginSerializer

from rest_framework_simplejwt.tokens import RefreshToken

from rest_framework.permissions import IsAuthenticated

from .serializers import ChangePasswordSerializer, ForgotPasswordSerializer, ResetPasswordSerializer

from .models import PasswordResetToken

from datetime import timedelta

from django.utils import timezone

from django.contrib.auth.models import User

from .permissions import IsAdmin, IsOwner

from .throttles import LoginRateThrottle, EmployeeRateThrottle, ReportRateThrottle

from .security import log_security_event

from rest_framework.permissions import AllowAny

class LoginAPIView(APIView):
    throttle_classes = [LoginRateThrottle]

    permission_classes = [AllowAny]
    
    def post(self, request):

        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        if serializer.is_valid():

            print(serializer.validated_data)
            user = serializer.validated_data.get("user")
            log_security_event(user,request,"LOGIN_SUCCESS","SUCCESS")

            response_data = serializer.validated_data.copy()
            response_data.pop("user", None)

            return Response(response_data,status=status.HTTP_200_OK)

        log_security_event(None,request,"LOGIN_FAILED","FAILED")

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
class RefreshTokenAPIView(APIView):
    permission_classes = [AllowAny]
    def post(self, request):
        refresh_token = request.data.get("refresh")
        
        if not refresh_token:
            return Response(
                {
                    "error": "Refresh token expired"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        try:
            refresh = RefreshToken(refresh_token)
            
            return Response(
                {
                    "access": str(refresh.access_token)
                },
                status = status.HTTP_200_OK
            )
        except Exception:
            return Response(
                {
                    "error": "Invalid Refresh Token"
                },
                status=status.HTTP_401_UNAUTHORIZED
            )
            
            
class LogoutAPIView(APIView):
    
    permission_classes = [IsAuthenticated]
    def post(self, request):
        refresh_token = request.data.get("refresh")
        if not refresh_token:
            return Response(
                {"error": "Refresh token is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            token = RefreshToken(refresh_token)
            token.blacklist()
            log_security_event(
                request.user,
                request,
                "TOKEN_BLACKLISTED",
                "SUCCESS"
            )

            return Response({"message": "Logout successful"},status=status.HTTP_200_OK)

        except Exception:
            return Response(
                {"error": "Invalid or expired refresh token"},
                status=status.HTTP_400_BAD_REQUEST
            )
            
class ChangePasswordAPIView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        serializer = ChangePasswordSerializer(data=request.data)

        if serializer.is_valid():
            user = request.user
            if not user.check_password(
                serializer.validated_data["old_password"]
            ):
                return Response(
                    {
                        "error": "Current password is incorrect"
                    },
                    status=status.HTTP_400_BAD_REQUEST
                )

            user.set_password(
                serializer.validated_data["new_password"]
            )

            user.save()
            log_security_event(request.user,request,"PASSWORD_CHANGE","SUCCESS")
            return Response({"message": "Password changed successfully"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
class ForgotPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ForgotPasswordSerializer(data=request.data)

        if serializer.is_valid():
            email = serializer.validated_data["email"]
            try:
                user = User.objects.get(email=email)
                reset_token = PasswordResetToken.objects.create(
                    user=user,
                    expires_at=timezone.now() + timedelta(minutes=15)
                )


                return Response(
                    {
                        "message": "Password reset token generated",
                        "token": str(reset_token.token)
                    },
                    status=status.HTTP_200_OK
                )


            except User.DoesNotExist:
                return Response(
                    {
                        "error": "User not found"
                    },
                    status=status.HTTP_404_NOT_FOUND
                )
        print("FORGOT PASSWORD ERORS:", serializer.errors)


        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
        
class RestPasswordAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = ResetPasswordSerializer(data=request.data)

        if serializer.is_valid():
            try:
                reset_token = PasswordResetToken.objects.get(
                    token=serializer.validated_data["token"]
                )

            except PasswordResetToken.DoesNotExist:
                return Response({"error": "Invalid reset token"},status=status.HTTP_400_BAD_REQUEST)

            if reset_token.is_expired():
                reset_token.delete()
                return Response({"error": "Reset token expired"},status=status.HTTP_400_BAD_REQUEST)
            
            user = reset_token.user
            user.set_password(serializer.validated_data["new_password"])
            user.save()

            log_security_event(
                user,
                request,
                "PASSWORD_RESET",
                "SUCCESS"
            )

            reset_token.delete()

            return Response({"message": "Password Reset successfully"},status=status.HTTP_200_OK)

        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
class EmployeeListAPIView(APIView):
    permission_classes = [IsAdmin]
    
    def get(self, request):
        return Response({"message": "Employee List"})
    
class UserProfileAPIView(APIView):
    permission_classes = [IsAuthenticated, IsOwner]

    def get(self, request):
        user = request.user
        self.check_object_permissions(request, user)
        return Response({
            "id": user.id,
            "username": user.username,
            "email": user.email
        })
        

class ReportAPIView(APIView):
    throttle_classes = [ReportRateThrottle]