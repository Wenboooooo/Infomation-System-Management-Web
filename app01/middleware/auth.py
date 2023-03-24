from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):
    """middleware 1"""
    def process_request(self, request):

        # Exclude those websites that do not need login to access
        # Get the url that the user requests
        if request.path_info in ["/login/", "/image/code/"]:
            return

        # If returns nothing(none), continue traversing middlewares
        # Or returns directly, stop traversing

        # Check the session info from the user, if get it successfully, the user can pass the middleware
        info_dict = request.session.get("info")
        # If the user has logged in
        if info_dict:
            return

        # If the user has not logged in
        return redirect("/login/")

