from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenVerifyView,
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path("api/auth/token", TokenObtainPairView.as_view(), name="login"),
    path("api/auth/token/refresh", TokenRefreshView.as_view()),
    path("api/auth/token/verify", TokenVerifyView.as_view()),
    path("api/users/", include("user.urls")),
    path("api/teams/", include("team.urls")),
    path("api/players/", include("player.urls")),
    path("api/matches/", include("match.urls")),
    path("admin/", admin.site.urls),
]
