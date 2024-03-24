from django.contrib import admin
from .models import GameListing, MatchListing

# Register your models here.
admin.site.register(GameListing)
admin.site.register(MatchListing)