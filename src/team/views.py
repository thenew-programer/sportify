from django.shortcuts import render
from rest_framework.views import APIView
from .models import Team

class RetrieveTeams(APIView):

    def get(self, request):
        teams = Team.objects.all()

        for team in teams

# Create your views here.
