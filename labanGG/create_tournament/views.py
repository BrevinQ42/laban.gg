from django.shortcuts import render, redirect
from .forms import TournamentForm
from .models import Tournament

def create_tournament(request):
    user = request.user
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            tournament = form.save(commit=False)
            tournament.game = form.cleaned_data['game']  # Associate with the selected game
            
            # Check if image is provided
            if 'image' not in request.FILES:
                # If no image provided, assign a default image
                tournament.image = "tournament_images/labanlogo.png"

            tournament.save()
            return redirect('/laban.gg/games')
    else:
        form = TournamentForm()
    return render(request, 'create_tournament.html', {'form': form, 'user': user})
