from rest_framework import serializers
from . import models


class APISerializer(serializers.ModelSerializer):
    class Meta:
        fields = "__all__"  ##creates all the fields in the serializer for #the registered model
        model = models.blogs.Blog  ##register model with the serializer
