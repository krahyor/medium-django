from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth import authenticate


def sign_in(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)

        if user is not None:

            login(request, user)
            return redirect("/")

    return render(request, "login/sign-in.html")


def register(request):
    return render(
        request,
        "login/register.html",
        {"next": request.GET.get("next")},
    )
