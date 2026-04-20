# blog/models.py
from django.db import models


class Post(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField()
    name = models.CharField(max_length=120)
    password = models.CharField(max_length=120)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
