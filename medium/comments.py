# blog/models.py
from django.db import models
from django.conf import settings


class Comment(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField()
    star = models.IntegerField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    created_by = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="updated_blogs"
    )

    blog = models.ForeignKey(
        "blogs.Blog", on_delete=models.CASCADE, related_name="comments"
    )

    def __str__(self):
        return self.title
