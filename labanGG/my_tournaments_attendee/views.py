from django.shortcuts import render
from join_tournament.models import TournamentPlayer
from create_tournament.models import Tournament

def my_tournaments_attendee(request):
    user = request.user
    user_tournaments = TournamentPlayer.objects.filter(account=user)

    # Fetch all tournaments
    all_tournaments = Tournament.objects.all()

    # Filter tournaments that the user has joined
    tournaments = [tournament.tournament for tournament in user_tournaments]

    context = {
        'tournaments': tournaments,
    }

    return render(request, 'my_tournaments_attendee.html', context)
