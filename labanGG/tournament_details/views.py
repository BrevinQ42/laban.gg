import random
from django.shortcuts import render, redirect
from create_tournament.models import Tournament
from register.models import Account
from join_tournament.models import TournamentPlayer
from .models import Bracket, Matchup, PlayerInMatchup

# Create your views here.
def tournament_details(request, id):
    context = {}

    tournament = Tournament.objects.get(id=id)
    
    user = request.user
    context['user'] = user
    context['base_template'] = 'base_organizer.html' if user.isOrganizer else 'base_attendee.html'

    if request.POST.get('updateTourneyStatus'):
        if tournament.status == "Upcoming":
            tournament.status = "Pending"
        elif tournament.status == "Pending":
            tournament.status = "Ongoing"
            GenerateMatchups(tournament)

        elif tournament.status == "Paused":
            tournament.status = "Ongoing"
        elif tournament.status == "Ongoing":
            tournament.status = "Paused"

        tournament.save()

    elif request.POST.get('notStartingYet'):
        tournament.status = "Upcoming"
        tournament.save()

    elif request.POST.get('goToJoinTourney'):
        return redirect(f'/tournament{id}/jointournament/')

    context['tournament'] = tournament

    return render(request, 'tournament_details.html', context)


# function that will generate the initial matchups for the tournament
def GenerateMatchups(tournament):
    winnersBracket = Bracket(tournament=tournament, classification="Winners")
    winnersBracket.save()

    if tournament.format == "double_elimination":
        losersBracket = Bracket(tournament=tournament, classification="Losers")
        losersBracket.save()

    players = TournamentPlayer.objects.filter(tournament=tournament)
    players = list(players.filter(application_status="Accepted"))
    random.shuffle(players)

    # first round matchups
    for i in range(0, len(players)-1, 2):
        matchup = Matchup(bracket=winnersBracket, matchNumber=(i//2)+1)
        matchup.save()

        player1 = PlayerInMatchup(player=players[i], matchup=matchup, playerNumber=1)
        player1.save()

        player2 = PlayerInMatchup(player=players[i+1], matchup=matchup, playerNumber=2)
        player2.save()