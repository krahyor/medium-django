from django.urls import include, path


from drf_yasg import openapi
from drf_yasg.views import get_schema_view

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
    path("v1/", include("medium.api.v1.urls"), name="v1"),
]
