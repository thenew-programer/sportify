from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.fields import related
from player.models import Player

User = get_user_model()


class Team(models.Model):
    """Generic Team Model for all types of sports, e-sports, and contests."""
    
    TEAM_CATEGORIES = [
        ('sports', 'Sports'),
        ('esports', 'eSports'),
        ('ctf', 'CTF Contest'),
        ('cp', 'Competitive Programming'),
        ('other', 'Other'),
    ]

    SPORT_TYPES = [
        ('football', 'Football'),
        ('basketball', 'Basketball'),
        ('volleyball', 'Volleyball'),
        ('tennis', 'Tennis'),
        ('chess', 'Chess'),
        ('fps', 'FPS Game'),
        ('moba', 'MOBA Game'),
        ('battle_royale', 'Battle Royale'),
        ('ctf', 'Capture The Flag'),
        ('cp', 'Competitive Programming'),
        ('other', 'Other'),
    ]

    name = models.CharField(max_length=255, unique=True)
    abbreviation = models.CharField(max_length=10, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    category = models.CharField(max_length=10, choices=TEAM_CATEGORIES, default='sports')
    sport_type = models.CharField(max_length=20, choices=SPORT_TYPES, default='other')
    wins = models.IntegerField(default=0)
    losses = models.IntegerField(default=0)
    draws = models.IntegerField(default=0)
    total_points = models.IntegerField(default=0)
    logo = models.ImageField(upload_to="team_logos/", blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.get_sport_type_display()})"

    def update_points(self, win_points=3, draw_points=1):
        """Update total points based on wins, draws, and losses."""
        self.total_points = (self.wins * win_points) + (self.draws * draw_points)
        self.save(using=self._db)

class TeamMembership(models.Model):
    """Intermediate model to link Players with Teams while ensuring only one team per sport per player."""
    
    player = models.ForeignKey(Player, on_delete=models.CASCADE, related_name="team_memberships")
    team = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="memberships")

    ROLE_CHOICES = [
        ('player', 'Player'),
        ('captain', 'Captain'),
        ('coach', 'Coach'),
        ('analyst', 'Analyst'),
        ('support', 'Support'),
        ('substitute', 'Substitute'),
        ('other', 'Other'),
    ]
    role = models.CharField(max_length=15, choices=ROLE_CHOICES, default='player')

    joined_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["player", "team"], name="unique_player_per_sport"
            )
        ]

    def __str__(self):
        return f"{self.player.first_name} - {self.team.name} ({self.get_role_display()})"
