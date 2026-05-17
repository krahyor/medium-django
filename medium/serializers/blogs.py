from rest_framework import serializers
from rest_framework_simplejwt.state import token_backend
from rest_framework_simplejwt.serializers import (
    TokenObtainPairSerializer,
    TokenRefreshSerializer,
)

from django.contrib.auth import get_user_model

from medium.models.blogs import Blog


class BlogSchema:
    def __init__(
        self,
        title,
        content,
        id=None,
        created_date=None,
        updated_date=None,
        created_by=None,
        updated_by=None,
    ):
        self.id = id
        self.title = title
        self.content = content
        self.created_date = created_date
        self.updated_date = updated_date
        self.created_by = created_by
        self.updated_by = updated_by


class BlogSerializer(serializers.ModelSerializer):
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)

    class Meta:
        model = Blog
        fields = [
            "id",
            "title",
            "content",
            "created_date",
            "updated_date",
            "created_by",
            "updated_by",
        ]
        read_only_fields = [
            "id",
            "created_date",
            "updated_date",
            "created_by",
            "updated_by",
        ]

    def create(self, validated_data):
        user = self.context["request"].user

        if not user.is_authenticated:
            user = None
        blog = Blog.objects.create(
            created_by=user,
            updated_by=user,
            **validated_data,
        )

        return BlogSchema(
            title=blog.title,
            content=blog.content,
        )
