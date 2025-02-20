from django.utils.deprecation import MiddlewareMixin

class CookieToAuthHeaderMiddleware(MiddlewareMixin):
    def process_request(self, request):
        unauthenticated_paths = {
            "/api/users/register",
            "/api/auth/token",
            "/api/auth/token/refresh",
            "/api/auth/token/verify",
            "/api/teams/",
            "/api/matches/",
            "/api/players/",
            "/api/players/players-by-sport/",
            "/api/players/players-by-team/"
        }
        if (request.path in unauthenticated_paths):
            return
        access_token = request.COOKIES.get("access_token")
        if access_token:
            request.META["HTTP_AUTHORIZATION"] = f"Bearer {access_token}"
