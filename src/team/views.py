from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView, status
from .serializers import TeamListSerializer, TeamSerializer
from .models import Team, TeamMembership


class RetrieveTeams(APIView):

    def get(self, request):
        try:
            data = Team.objects.all()
            teams = TeamListSerializer(data, many=True)
            return Response({"teams":teams.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"error": "Something went wrong when retrieving teams"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )

class CreateTeam(APIView):
    """Create a new team and assign selected players"""

    def post(self, request):
        try:
            if not request.user.is_admin:
                return Response(
                    {"error": "Only admins can create teams"},
                    status=status.HTTP_401_UNAUTHORIZED
                )

            data = request.data
            player_logins = data.get("players", [])

            if len(player_logins) != 7:
                return Response(
                    {"error": "You must select exactly 7 players."},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            serializer = TeamSerializer(data=data)
            
            if serializer.is_valid():
                team = serializer.save()
                
                from player.models import Player
                players = Player.objects.filter(id__in=player_logins)
                if players.count() != 7:
                    return Response(
                        {"error": "Some selected players do not exist."},
                        status=status.HTTP_400_BAD_REQUEST,
                    )

                for player in players:
                    TeamMembership.objects.create(player=player, team=team, role="player")

                return Response(
                    {
                        "success": "Team registered successfully with selected players",
                        "team": serializer.data,
                    },
                    status=status.HTTP_201_CREATED,
                )
            else:
                return Response(
                    {"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST
                )
        except Exception as e:
            print(e)
            return Response(
                {"error": "Something went wrong"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
