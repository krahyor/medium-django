from rest_framework import serializers
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from django.contrib.auth import get_user_model

from medium.models.blogs import Blog


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    def create(self, validated_data):
        user = self.context["request"].user
        blog = Blog.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data,
        )
        return blog

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
        ]
        read_only_fields = [
            "id",
            "created_date",
            "updated_date",
            "created_by",
            "updated_by",
        ]
