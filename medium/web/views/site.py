import requests
from django.shortcuts import redirect
from django.template.response import TemplateResponse

from medium.models.blogs import Blog


def index(request):
    return TemplateResponse(request, "index/index.html")


def create_blog(request):
    return TemplateResponse(request, "index/create.html")


def edit_blog(request, pk):
    blog = Blog.objects.get(pk=pk)
    return TemplateResponse(request, "index/edit.html", {"blog": blog, "pk": pk})
