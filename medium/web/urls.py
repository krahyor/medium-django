from django.urls import include, path


from medium.web.views import accounts, site

urlpatterns = [
    path("", site.index, name="index"),
    path("register/", accounts.register, name="register"),
    path("sign-in/", accounts.sign_in, name="sign-in"),
]
