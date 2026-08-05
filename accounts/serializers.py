from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers

from django.contrib.auth import authenticate

from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = [
            "username",
            "email",
            "password",
            "phone",
            "role",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"),
            password=validated_data["password"]
        )
        return user
class LoginSerializer(serializers.Serializer):
    username =  serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, attrs):
        user = authenticate(
            username=attrs["username"],
            password=attrs["password"]
        )

        if not user:
            raise serializers.ValidationError("Invalid Credentials")

        refresh = RefreshToken.for_user(user)

        return {
            "user":user.username,
            'role':user.role,
            "access":str(refresh.access_token),
            "refresh": str(refresh)
        }