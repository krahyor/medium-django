def login(request):
    return render(
        request,
        "login/login.html",
        {"form": AuthenticationForm(), "next": request.GET.get("next")},
    )
