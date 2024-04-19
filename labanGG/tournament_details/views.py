from django.shortcuts import render, redirect
from create_tournament.models import Tournament
from register.models import Account
from join_tournament.views import join_tournament
from join_tournament.models import TournamentPlayer

# Create your views here.
def tournament_details(request, id):
    user = request.user
    td = Tournament.objects.get(id=id)
 
    return render(request, 'tournament_details.html', {'tournament': td, 'user':user})
    
def join_tournament(request, id):
    tournament = Tournament.objects.get(id=id)
    user = request.user
    if user.isOrganizer == True:
        return redirect('/log_in/')
    if request.method == 'POST':
        accountUser = user.username
        ign = request.POST.get('ign')
        age = request.POST.get('age')
        country = request.POST.get('country')

        jt = TournamentPlayer(ign=ign, age=age, country=country, accountUser=accountUser, account=user, tournament=tournament)
        jt.save()

        return render(request, 'join_tournament.html', {'join_tournament': jt, 'user':user})
    
    return render(request, 'join_tournament.html', {'user': user})
