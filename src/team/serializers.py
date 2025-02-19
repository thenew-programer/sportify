from rest_framework import serializers
from .models import Team


class TeamListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
            "sport_type",
            "category",
            "wins",
            "losses",
        )
