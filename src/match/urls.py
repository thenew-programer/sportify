from django.urls import path
from match.views import ListMatchesView, CreateMatchView

urlpatterns = [
    path("", ListMatchesView.as_view()),
    path("create", CreateMatchView.as_view())
]
