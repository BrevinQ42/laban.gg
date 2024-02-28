from django.shortcuts import render, redirect
from .forms import TournamentForm

def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('tournament_list')  # Redirect to a page showing all tournaments
    else:
        form = TournamentForm()
    return render(request, 'create_tournament.html', {'form': form})
