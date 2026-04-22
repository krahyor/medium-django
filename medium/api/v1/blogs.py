from rest_framework import generics

from medium.api.serializers.blogs import BlogSerializer
from medium.models.blogs import Blog


class BlogListCreateAPIView(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
