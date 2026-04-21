from django.shortcuts import redirect

from django.template.response import TemplateResponse


def index(request):
    return TemplateResponse(request, "index/index.html", {"title": "Index Page"})
