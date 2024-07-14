from django.shortcuts import render, redirect
from .models import League, Team, Player

from . import team_maker


def index(request):
    context = {
        # Query 1: All baseball leagues
        "baseball_leagues": League.objects.filter(sport__icontains="baseball"),
        # Query 2: All women's leagues
        "womens_leagues": League.objects.filter(name__icontains="women"),
        # Query 3: All leagues where sport is any type of hockey
        "hockey_leagues": League.objects.filter(sport__icontains="hockey"),
        # Query 4: All leagues where sport is something OTHER THAN football
        "non_football_leagues": League.objects.exclude(sport__icontains="football"),
        # Query 5: All leagues that call themselves "conferences"
        "conference_leagues": League.objects.filter(name__icontains="conference"),
        # Query 6: All leagues in the Atlantic region
        "atlantic_leagues": League.objects.filter(name__icontains="atlantic"),
        # Query 7: All teams based in Dallas
        "dallas_teams": Team.objects.filter(location__icontains="dallas"),
        # Query 8: All teams named the Raptors
        "raptors_teams": Team.objects.filter(team_name__icontains="raptors"),
        # Query 9: All teams whose location includes "City"
        "city_teams": Team.objects.filter(location__icontains="city"),
        # Query 10: All teams whose names begin with "T"
        "t_teams": Team.objects.filter(team_name__startswith="T"),
        # Query 11: All teams, ordered alphabetically by location
        "teams_by_location": Team.objects.all().order_by("location"),
        # Query 12: All teams, ordered by team name in reverse alphabetical order
        "teams_by_name_reverse": Team.objects.all().order_by("-team_name"),
        # Query 13: Every player with last name "Cooper"
        "cooper_players": Player.objects.filter(last_name__icontains="cooper"),
        # Query 14: Every player with first name "Joshua"
        "joshua_players": Player.objects.filter(first_name__icontains="joshua"),
        # Query 15: Every player with last name "Cooper" EXCEPT those with "Joshua" as the first name
        "cooper_not_joshua": Player.objects.filter(last_name__icontains="cooper").exclude(first_name__icontains="joshua"),
        # Query 16: All players with first name "Alexander" OR first name "Wyatt"
        "alexander_or_wyatt_players": Player.objects.filter(first_name__in=["Alexander", "Wyatt"]),
    }
    return render(request, "leagues/index.html", context)

def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")

# leagues/views.py
from django.shortcuts import render
from .models import League, Team, Player

