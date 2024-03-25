from django.contrib import admin
from .models import GameListing, MatchListing
from django_summernote.admin import SummernoteModelAdmin

@admin.register(GameListing)
class PostAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('game_name',)}

# Register your models here.
admin.site.register(MatchListing)