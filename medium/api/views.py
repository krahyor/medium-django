from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from medium import serializers
from medium.models.blogs import Blog


class BlogAPIView(APIView):
    def get(self, request, format=None):

        blogs = Blog.objects.all()
        serializer = serializers.APISerializer(blogs, many=True)
        print(serializer.data)
        return Response(serializer.data)
