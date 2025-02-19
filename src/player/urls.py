from django.urls import path

from player.views import RegisterPlayer, RetrievePlayers, RetrievePlayersBySport

urlpatterns = [
    path("players", RetrievePlayers.as_view()),
    path("create", RegisterPlayer.as_view()),
    path("players-by-sport/?sport_type=football", RetrievePlayersBySport.as_view()),
]
