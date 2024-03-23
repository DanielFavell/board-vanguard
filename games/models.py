from django.db import models
from django.contrib.auth.models import User

PLAYERS = (("Yourself"), ("Opponent"))

# Create your models here.
class Games(models.Model):
    game_name = models.CharField(max_length=200, unique=True)
    description = models.TextField()

class Matches(models.Model):
    game_id = models.ForeignKey(Games, on_delete=models.CASCADE, related_name="match_list")
    first_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_played")
    time_created = models.DateTimeField(auto_now_add=True)
    opponent = models.CharField(max_length=200)
    winner = models.CharField(max_length=200, choices=PLAYERS)