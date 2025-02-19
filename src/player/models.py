from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Player(models.Model):
    """Represents a player in a team. A player might or might not be a registered User."""
    
    PLAYER_POSITIONS = [
        ('goalkeeper', 'Goalkeeper'),
        ('defender', 'Defender'),
        ('midfielder', 'Midfielder'),
        ('forward', 'Forward'),
        ('captain', 'Captain'),
        ('support', 'Support'),
        ('carry', 'Carry'),
        ('analyst', 'Analyst'),
        ('coach', 'Coach'),
        ('other', 'Other'),
    ]
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="player_profile")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    nickname = models.CharField(max_length=100, blank=True, null=True)  # Optional in-game or competition name
    age = models.PositiveIntegerField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    position = models.CharField(max_length=20, choices=PLAYER_POSITIONS, default='other')
    bio = models.TextField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to="player_profiles/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.nickname or self.first_name} - {self.get_position_display()}"
