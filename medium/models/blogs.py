# blog/models.py
from django.db import models
from django.conf import settings


class Blog(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="updated_blogs",
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.title


class BlogComment(models.Model):
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default="active")
    blog = models.ForeignKey(
        Blog, on_delete=models.CASCADE, related_name="blog_comments"
    )

    def __str__(self):
        return self.content
