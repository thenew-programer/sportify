from rest_framework.views import APIView
from rest_framework.response import Response
from player.models import Player
from .serializers import PlayerSerializer
from rest_framework import status, permissions


class RegisterPlayer(APIView):
    def post(self, request):
        try:
            data = request.data
            user = request.user
            serializer = PlayerSerializer(data=data)
            if serializer.is_valid():
                print("saving saving....")
                serializer.save(user=user)
                return Response(
                    {
                        "success": "Player registered successfully",
                        "player": serializer.data,
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
                {"error": "Something went wrong when registring a player"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetrievePlayers(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            players = Player.objects.all()
            serializer = PlayerSerializer(players, many=True)
            return Response({"players": serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            print(e)
            return Response(
                {"error": "Something went wrong when retrieving players"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class RetrievePlayersBySport(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request):
        try:
            sport_type = request.query_params.get("sport_type")

            if not sport_type:
                return Response(
                    {"error": "sport_type query parameter is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            players = Player.objects.filter(sport_type=sport_type)

            if not players.exists():
                return Response(
                    {"message": "No players found for this sport type"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            serializer = PlayerSerializer(players, many=True)
            return Response({"players": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class RetrievePlayersByTeam(APIView):
    permission_classes = (permissions.AllowAny,)
    def get(self, request, team_name):
        try:
            if not team_name:
                return Response(
                    {"error": "team_name query parameter is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            from team.models import Team
            team = Team.objects.filter(name=team_name).first()
            if not team:
                return Response(
                    {"message": "No teeam found for this sport type"},
                    status=status.HTTP_404_NOT_FOUND,
                )

            from team.models import TeamMembership
            players = Player.objects.filter(id__in=TeamMembership.objects.filter(team=team).values_list('player', flat=True))


            serializer = PlayerSerializer(players, many=True)
            return Response({"players": serializer.data}, status=status.HTTP_200_OK)

        except Exception as e:
            print(e)
            return Response(
                {"error": f"Something went wrong: {str(e)}"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

class RetrievePlayer(APIView):
    def get(self, request):
        try:
            user = request.user
            player = Player.objects.filter(login=user.login)
            if not player.exists():
                return Response(
                    {"is_player": "false"}
                    status=status.HTTP_200_OK
                )
            else:
                return Response(
                    {"is_player": "true"}
                    status=status.HTTP_200_OK
                )

            return Response({"user": user.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Something went wrong when retrieving user details"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

