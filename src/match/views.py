from rest_framework.views import APIView
from .serializers import MatchSerializer
from rest_framework.response import Response
from rest_framework import status, permissions
from .models import Match


class CreateMatchView(APIView):
    """Create a new match"""

    def post(self, request):
        serializer = MatchSerializer(data=request.data)
        if serializer.is_valid():
            match = serializer.save()
            return Response(
                {"success": "Match created successfully", "match": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListMatchesView(APIView):
    """Retrieve all matches or filter by status"""
    permission_classes = (permissions.AllowAny, )

    def get(self, request):
        status_filter = request.query_params.get("status")
        if status_filter:
            matches = Match.objects.filter(status=status_filter)
        else:
            matches = Match.objects.all()

        serializer = MatchSerializer(matches, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
