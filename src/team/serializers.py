from rest_framework import serializers
from .models import Team, TeamMembership


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
            "sport_type",
            "wins",
            "losses",
            "draws",
        )

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
        )
