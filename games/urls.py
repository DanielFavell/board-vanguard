from . import views
from django.urls import path

urlpatterns = [
    path("", views.home_page, name="home"),
    path("new_match/", views.new_match, name="add_new_match"),
    path("games/", views.GameList.as_view(), name="game_list"),
    path("<slug:slug>/", views.game_detail, name="game_detail"),
    path("<slug:slug>/match_history", views.MatchHistory.as_view(), name="match_history"),
]