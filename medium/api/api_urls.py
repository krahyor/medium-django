from django.urls import include, path


from medium.api import views

urlpatterns = [
    path("", views.BlogAPIView.as_view(), name="blogs-api"),
]
