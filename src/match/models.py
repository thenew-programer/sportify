from django.db import models
from team.models import Team

class Match(models.Model):

    STATUS_CHOICES = [
        ("scheduled", "Scheduled"),
        ("completed", "Completed"),
        ("cancelled", "Cancelled"),
    ]
    team1 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="home_matches")
    team2 = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="away_matches")
    match_date = models.DateTimeField()
    team1_score = models.PositiveIntegerField(default=0)
    team2_score = models.PositiveIntegerField(default=0)
    winner = models.ForeignKey(Team, on_delete=models.SET_NULL, null=True, blank=True, related_name="won_matches")
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="scheduled")

    def determine_winner(self):
        """Determine the winner based on scores"""
        if self.team1_score > self.team2_score:
            self.winner = self.team1
        elif self.team2_score > self.team1_score:
            self.winner = self.team2
        else:
            self.winner = None
        self.save()

    def __str__(self):
        return f"{self.team1.name} vs {self.team2.name} on {self.match_date.strftime('%Y-%m-%d')}"

