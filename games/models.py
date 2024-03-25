from django.db import models
from django.contrib.auth.models import User

PLAYERS = ((0,"Yourself"), (1,"Opponent"))

# Create your models here.
class GameListing(models.Model):
    game_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=250, unique=True, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return f"{self.game_name}"

class MatchListing(models.Model):
    game_id = models.ForeignKey(GameListing, on_delete=models.CASCADE, related_name="match_list")
    first_player = models.ForeignKey(User, on_delete=models.CASCADE, related_name="matches_played")
    time_created = models.DateTimeField(auto_now_add=True)
    opponent = models.CharField(max_length=200)
    winner = models.IntegerField(choices=PLAYERS, default=0)