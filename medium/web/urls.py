from django.urls import include, path


from medium.web.views import accounts, site

urlpatterns = [
    path("", site.index, name="index"),
    path("create-blog/", site.create_blog, name="create-blog"),
    path("edit_blog/<int:pk>/", site.edit_blog, name="edit-blog"),
    path("register/", accounts.RegisterView.as_view(), name="register"),
    path("sign-in/", accounts.SignInView.as_view(), name="sign-in"),
]
