from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .forms import NewGame, NewMatch
from .models import GameListing, MatchListing

# Create your views here.
def home_page(request):
    return render(
        request,
        "games/index.html"
    )

class GameList(generic.ListView):
    model = GameListing
    queryset = GameListing.objects.all()
    template_name = "current_games.html"

def game_detail(request, slug):
    queryset = GameListing.objects.all()
    game = get_object_or_404(queryset, game_name=slug)
    return render(
        request,
        "games/game_detail.html",
        {
            "game": game,
        }
    )

class MatchHistory(generic.ListView):
    model = MatchListing
    queryset = GameListing.objects.all()
    template_name = "match_history.html"

def new_match(request):
    if request.method == "POST":
        match_form = NewMatch(request.POST)
        if match_form.is_valid():
            match = match_form.save(commit=False)
            match.first_player = request.user
            match.save()
            messages.success(request, "You have added a new match result")
            return redirect("success/")
    else:
        match_form = NewMatch()

    return render(request, "games/add_match.html", {"match_form":match_form})