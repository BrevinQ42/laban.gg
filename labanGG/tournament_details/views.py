from django.shortcuts import render, redirect
from create_tournament.models import Tournament
from register.models import Account
from join_tournament.views import join_tournament
from join_tournament.models import TournamentPlayer

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
        elif tournament.status == "Pending" or tournament.status == "Paused":
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
