from django.urls import path


from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from medium.api.views import AccountRegisterView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

schema_view = get_schema_view(
    openapi.Info(
        title="Swagger API",
        default_version="v1",
    ),
    public=True,
)

urlpatterns = [
    path(
        "docs/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="redoc-schema",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="swagger-schema",
    ),
    path("register/", AccountRegisterView.as_view()),
    path("login/", TokenObtainPairView.as_view()),
    path("refresh/", TokenRefreshView.as_view()),
]
