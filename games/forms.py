from .models import GameListing, MatchListing
from django import forms

class NewGame(forms.ModelForm):
    class Meta:
        model = GameListing
        fields = ("game_name","description",)

class NewMatch(forms.ModelForm):
    class Meta:
        model = MatchListing
        fields = ("game_id", "opponent", "winner",)
