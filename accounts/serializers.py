from rest_framework import serializers
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate
from django.contrib.auth.password_validation import validate_password

from rest_framework.exceptions import AuthenticationFailed

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=True)
    password = serializers.CharField(required=True)

    def validate(self, data):
        username = data.get("username")
        password = data.get("password")

        print("USERNAME:", username)
        print("PASSWORD:", password)

        user = authenticate(
            username=username,
            password=password
        )

        print("AUTH RESULT:", user)

        if user is None:
            raise AuthenticationFailed(
                "Invalid username or password"
            )

        refresh = RefreshToken.for_user(user)

        return {
            "user": user,
            "username": user.username,
            "access": str(refresh.access_token),
            "refresh": str(refresh),
        }
class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    
    def validate_new_password(self, value):
        validate_password(value)
        return value
    
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()
    
    
class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.UUIDField()
    new_password = serializers.CharField(write_only=True)
    
    def validate_new_password(self, value):
        validate_password(value)
        return value
    