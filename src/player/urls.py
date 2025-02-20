from django.urls import path
from player.views import RegisterPlayer, RetrievePlayers, RetrievePlayersBySport, RetrievePlayersByTeam, RetrievePlayer

urlpatterns = [
    path("", RetrievePlayers.as_view()),
    path("me/", RetrievePlayer.as_view()),
    path("create/", RegisterPlayer.as_view()),
    path("players-by-sport/<str:sport_type>", RetrievePlayersBySport.as_view()),
    path("players-by-team/<str:team_name>", RetrievePlayersByTeam.as_view()),
]
