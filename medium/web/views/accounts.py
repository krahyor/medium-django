from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate

from medium.serializers import LoginSerializer, RegisterSerializer


class SignInView(View):
    template_name = "login/sign-in.html"

    def get(self, request):
        return render(request, self.template_name)

    def post(self, request):
        serializer = LoginSerializer(data=request.POST)

        if serializer.is_valid():
            user = authenticate(
                request,
                username=request.POST.get("username"),
                password=request.POST.get("password"),
            )
            if user is not None:
                login(request, user)
                return redirect("/")

        return render(request, self.template_name, {"errors": serializer.errors})


class RegisterView(View):
    template_name = "login/register.html"

    def get(self, request):
        return render(request, self.template_name, {"next": request.GET.get("next")})

    def post(self, request):
        serializer = RegisterSerializer(data=request.POST)
        if serializer.is_valid():
            serializer.save()
            return redirect("sign-in")
        return render(
            request,
            self.template_name,
            {
                "next": request.GET.get("next"),
                "errors": serializer.errors,
            },
        )


class AccountView(View):
    def get(self, request):
        return render(request, "accounts/account.html")

    def post(self, request):
        return render(request, "accounts/account.html")
