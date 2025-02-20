from rest_framework import serializers
from match.models import Match
from team.models import Team

class MatchSerializer(serializers.ModelSerializer):
    team1 = serializers.CharField(write_only=True)  # Accepts team name
    team2 = serializers.CharField(write_only=True)  # Accepts team name
    team1_name = serializers.SerializerMethodField(read_only=True)
    team2_name = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Match
        fields = "__all__"

    def get_team1_name(self, obj):
        return obj.team1.name if obj.team1 else None

    def get_team2_name(self, obj):
        return obj.team2.name if obj.team2 else None

    def create(self, validated_data):
        team1_name = validated_data.pop("team1")
        team2_name = validated_data.pop("team2")

        if (team1_name == team2_name):
            raise ValidationError("A team cannot play against itself.")
        team1 = Team.objects.filter(name=team1_name).first()
        team2 = Team.objects.filter(name=team2_name).first()

        if not team1 or not team2:
            raise serializers.ValidationError({"error": "One or both teams not found."})

        match = Match.objects.create(team1=team1, team2=team2, **validated_data)
        return match
