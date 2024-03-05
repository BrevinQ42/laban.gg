from django.shortcuts import render, redirect
from .forms import TournamentForm
from .models import Tournament

def create_tournament(request):
    if request.method == 'POST':
        form = TournamentForm(request.POST, request.FILES)
        if form.is_valid():
            # Check if image is provided
            if 'image' not in request.FILES:
                # If no image provided, assign a default image
                form.instance.image = "https://i.gyazo.com/cbb5ad244a3e28c3dd89906f62f179fe.png"  

            form.save()
            return redirect('tournament_list')  # Redirect to a page showing all tournaments
    else:
        form = TournamentForm()
    return render(request, 'create_tournament.html', {'form': form})
