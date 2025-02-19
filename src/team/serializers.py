from rest_framework import serializers
from .models import Team


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = (
            "name",
            "category",
            "sport_type",
            "wins",
            "losses",
        )
