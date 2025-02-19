from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import TeamListSerializer
from user.serializers import UserSerializer
from .models import Team


class RetrieveTeams(APIView):

    def get(self, request):
        user = request.data
        data = Team.objects.all()
        teams = []

        user = UserSerializer(user)
        for team in data:
            teams.append(TeamListSerializer(team))
        print(user.data)
        print(teams)
