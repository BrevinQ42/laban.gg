from django.shortcuts import render, redirect
from create_tournament.models import Tournament
from register.models import Account
from join_tournament.views import join_tournament
from join_tournament.models import TournamentPlayer

# Create your views here.
def tournament_details(request):
    user = request.user
    if request.method == 'POST':
        tournament_organizer = request.POST.get('tournament_organizer')
        name = request.POST.get('name')
        game = request.POST.get('game')
        tier = request.POST.get('tier')
        location = request.POST.get('location')
        format = request.POST.get('format')
        application_link = request.POST.get('application_link')
        schedule = request.POST.get('schedule')
        prize_pool = request.POST.get('prize_pool')
        more_details = request.POST.get('more_details')
        status = request.POST.get('status')


        td = Tournament(tournament_organizer=tournament_organizer, name=name, game=game, tier=tier, location=location, format=format, application_link=application_link, schedule=schedule, prize_pool=prize_pool, more_details=more_details, status=status)
        td.save()

        return render(request, 'tournament_details.html', {'tournament_details': td, 'user':user})
    
    return render(request, 'tournament_details.html', {'user': user})

def join_tournament(request):
    user = request.user
    if user.isOrganizer == True:
        return redirect('/log_in/')
    if request.method == 'POST':
        accountUser = user.username
        ign = request.POST.get('ign')
        age = request.POST.get('age')
        country = request.POST.get('country')

        jt = TournamentPlayer(ign=ign, age=age, country=country, accountUser=accountUser, account=user)
        jt.save()

        return render(request, 'join_tournament.html', {'join_tournament': jt, 'user':user})
    
    return render(request, 'join_tournament.html', {'user': user})
