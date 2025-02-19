from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

urlpatterns = [
    path("api/auth/token", TokenObtainPairView.as_view()),
    path("api/auth/token/refresh", TokenRefreshView.as_view()),
    path("api/auth/token/verify", TokenVerifyView.as_view()),
    path("api/users/", include("user.urls")),
    path("api/t/", include("team.urls")),
    path("api/p/", include("player.urls")),
    path("admin/", admin.site.urls),
]
