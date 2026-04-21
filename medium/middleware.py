from django.conf import settings
from django.shortcuts import redirect

ROUTE_LOGIN = ["/sign-in/", "/register/"]


class SteinDebugMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.website = {
            "url": "https://www.medium.com",
            "debug": settings.DEBUG,
        }

    def __call__(self, request):
        print("SteinDebugMiddleware: Request path:", request.path)
        response = self.get_response(request)

        if request.user.is_authenticated and request.path in ROUTE_LOGIN:
            print("User is authenticated, redirecting to home page")
            return redirect("/")

        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        print("Process view in SteinDebugMiddleware")
        print("View function:", view_func.__name__)
        return

    def process_template_response(self, request, response):
        response.context_data = {}
        if settings.DEBUG:

            response.context_data["website_url"] = self.website

        return response
