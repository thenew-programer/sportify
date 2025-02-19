from rest_framework.serializers import ModelSerializer, ValidationError
from player.models import Player


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = Player
        fields = "__all__"
        extra_kwargs = {
            "user": {"read_only": True},  # User is automatically assigned in the view
            "created_at": {"read_only": True},
            "updated_at": {"read_only": True},
        }

    def validate_sport_type(self, value):
        valid_sports = dict(Player.SPORT_TYPES).keys()
        if value not in valid_sports:
            raise ValidationError("Invalid sport type")
        return value
