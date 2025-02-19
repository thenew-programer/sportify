from rest_framework.views import APIView
from rest_framework.response import Response
from player.models import Player
from .serializers import PlayerSerializer
from rest_framework import status


class RegisterPlayer(APIView):
    def post(self, request):
        try:
            data = request.data
            user = request.user
            serializer = PlayerSerializer(data=data, files=request.FILES)
            if serializer.is_valid():
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
        except:
            return Response(
                {"error": "Something went wrong when registring a player"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetrievePlayers(APIView):
    def get(self, request):
        try:
            players = Player.objects.all()
            serializer = PlayerSerializer(data=players, many=True)
            return Response({"players": serializer.data}, status=status.HTTP_200_OK)
        except:
            return Response(
                {"error": "Something went wrong when retrieving players"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RetrievePlayersBySport(APIView):
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
