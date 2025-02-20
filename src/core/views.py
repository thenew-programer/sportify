# from rest_framework.views import APIView
# from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
# from rest_framework.response import Response
# from rest_framework import status
# from user.models import User
#
# class LoginView(TokenObtainPairView):
#     def post(self, request, *args, **kwargs):
#         response = super().post(request, *args, **kwargs)  # Get the default response
#         if response.status_code == 200:
#             data = response.data
#             access_token = data.get("access")
#             refresh_token = data.get("refresh")
#
#             response.set_cookie(
#                 key="access_token",
#                 value=access_token,
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#                 max_age=60 * 60 * 12, 
#             )
#             response.set_cookie(
#                 key="refresh_token",
#                 value=refresh_token,
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#                 max_age=60 * 60 * 24 * 7,
#             )
#
#             response.data.pop("access", None)
#             response.data.pop("refresh", None)
#             user = User.objects.filter(login=request.data["login"]).first()
#             response.data["user"] = {
#                 "login": user.login,
#                 "is_admin": user.is_admin,  # Assuming 'is_admin' is a field in the user model
#             }
#
#         return response
#
# class RefreshToken(TokenRefreshView):
#     def post(self, request, *args, **kwargs):
#         refresh_token = request.COOKIES.get("refresh_token")
#         if not refresh_token:
#             return Response({"error": "Refresh token missing"}, status=400)
#
#         request.data["refresh"] = refresh_token
#         response = super().post(request, *args, **kwargs)
#         if response.status_code == 200:
#             access_token = response.data.get("access")
#             response.set_cookie(
#                 key="access_token",
#                 value=access_token,
#                 httponly=True,
#                 secure=True,
#                 samesite="Lax",
#                 max_age = 60 * 60 * 2,
#             )
#             response.data["access_token"] = access_token
#         return response
#
# class LogoutView(APIView):
#     def post(self, request):
#         response = Response({"message": "Logged out successfully"}, status=status.HTTP_200_OK)
#
#         response.delete_cookie("access_token")
#         response.delete_cookie("refresh_token")
#         return response
