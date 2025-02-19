from django.urls import path
from .views import CreateTeam, RetrieveTeams

urlpatterns = [
    path("teams", RetrieveTeams.as_view()),
    path("create", CreateTeam.as_view()),
]
