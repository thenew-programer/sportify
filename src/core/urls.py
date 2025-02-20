from django.contrib import admin
from django.urls import path, include
from core.views import LoginView, LogoutView, RefreshToken
from rest_framework_simplejwt.views import (
    TokenVerifyView,
)

urlpatterns = [
    path("api/auth/token", LoginView.as_view(), name="login"),
    path("api/auth/token/refresh", RefreshToken.as_view()),
    path("api/auth/token/verify", TokenVerifyView.as_view()),
    path("api/auth/logout", LogoutView.as_view()),
    path("api/users/", include("user.urls")),
    path("api/teams/", include("team.urls")),
    path("api/players/", include("player.urls")),
    path("api/matches/", include("match.urls")),
    path("admin/", admin.site.urls),
]
