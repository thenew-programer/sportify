from django.utils.deprecation import MiddlewareMixin

class CookieToAuthHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if (request.path == '/api/users/register' or
            request.path == '/api/p/players'
        ):
            return
        access_token = request.COOKIES.get("access_token")
        if access_token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"
