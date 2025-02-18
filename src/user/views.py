from http.client import ResponseNotReady
from django.contrib.auth import get_user_model
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework import permissions, status
from .serializers import UserSerializer

User = get_user_model()


class RegisterView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request: Request):
        try:
            data = request.data

            try:
                login = data["login"]
                login = login.lower()
            except:
                return Response(
                    {"error", "Login field is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                password = data["password"]
            except:
                return Response(
                    {"error", "Password field is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            try:
                re_password = data["re_password"]
            except:
                return Response(
                    {"error", "Re_Password field is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            if password == re_password:
                if len(password) >= 8:
                    if not User.objects.filter(login=login).exists():
                        User.objects.create_user(login=login, password=password)
                        return Response(
                            {"success": "Spectator account created successfully"},
                            status=status.HTTP_201_CREATED,
                        )
                    else:
                        return Response(
                            {"error": "User with this login already exists"},
                            status=status.HTTP_400_BAD_REQUEST,
                        )
                else:
                    return Response(
                        {"error": "Password must be at least 8 characters in length"},
                        status=status.HTTP_400_BAD_REQUEST,
                    )
            else:
                return Response(
                    {"error": "Passwords do not match"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
        except:
            return Response(
                {"error": "Something went wrong when registering an account"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetrieveUserView(APIView):
    def get(self, request, format=None):
        try:
            user = request.user
            user = UserSerializer(user)

            return Response({"user": user.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Something went wrong when retrieving user details"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
