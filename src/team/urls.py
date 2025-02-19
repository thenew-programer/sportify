from django.urls import path
from .views import RetrieveTeams

urlpatterns = [
    path("teams", RetrieveTeams.as_view()),
]
