from rest_framework import serializers
from medium.models import *
from django.contrib.auth import get_user_model
from medium.common.utils import is_valid_email
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)
from rest_framework_simplejwt.state import token_backend
from medium.models.users import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_username(self, value):
        if not is_valid_email(value):
            raise serializers.ValidationError("invalid_email")
        return value

    def validate(self, data):
        if data["password"] != data["confirm_password"]:
            raise serializers.ValidationError("password_dont_match")

        data["password"] = data["password"]

        data.pop("password", None)
        data.pop("confirm_password", None)

        return data

    class Meta:
        model = get_user_model()
        fields = [
            "id",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
            "username",
        ]
        read_only_fields = [
            "id",
        ]


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            "first_name",
            "last_name",
            "username",
            "role",
        )
        read_only_fields = ["username", "role", "expiration_date"]


class LoginSerializer(TokenObtainPairSerializer):

    def validate(self, attrs):
        username = attrs["username"]
        user = get_user_model().objects.filter(username=username).first()

        if not user or not user.check_password(attrs["password"]):
            raise serializers.ValidationError("invalid_credentials")

        if not user.is_active:
            raise serializers.ValidationError("not_active")

        refresh = self.get_token(user)

        data = {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": UserSerializer(user).data,
            "role": user.role,
        }

        return data


class RefreshTokenSerializer(TokenRefreshSerializer):

    def validate(self, attrs):
        data = super().validate(attrs)
        decoded_payload = token_backend.decode(data["access"], verify=True)
        user_id = decoded_payload["user_id"]
        user = User.objects.get(id=user_id)
        data["role"] = user.role
        data["user"] = UserSerializer(user).data
        return data


class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
