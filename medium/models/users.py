from django.contrib.auth.models import AbstractUser
from django.db import models
import random
import datetime


class User(AbstractUser):
    userTypes = (
        ("admin", "Admin"),
        ("customer", "Customer"),
    )
    name = models.CharField(max_length=120, blank=True)
    role = models.CharField(choices=userTypes, default="customer", max_length=20)

    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username


class VerificationCode(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6, default=random.randint(111111, 999999))
    email = models.EmailField()
    expiration_date = models.DateTimeField(
        default=datetime.datetime.now() + datetime.timedelta(days=1)
    )

    def __str__(self):
        return self.user.username
