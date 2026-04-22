from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from medium.api.v1 import accounts, blogs

urlpatterns = [
    path("register/", accounts.AccountRegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
    path("blogs/", blogs.BlogListCreateAPIView.as_view()),
]
