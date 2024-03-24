# views.py
from django.shortcuts import render, redirect
from register.models import Account  
from create_tournament.models import Tournament

def my_tournaments_organizer(request):
    user = request.user
    if user.isOrganizer == True:
        organizerName = user.username
        tournaments = Tournament.objects.filter(tournament_organizer=organizerName)
        return render(request, 'my_tournaments_organizer.html', {'tournaments': tournaments})
    else:
        # Handle the case where the user is not a Tournament Organizer
        return redirect('/games/')
