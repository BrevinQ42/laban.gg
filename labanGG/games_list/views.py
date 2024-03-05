from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from .models import Game

class GamesListView(ListView):
    model = Game
    template_name = 'games_list/index.html'

class GamesDetailView(DetailView):
    model = Game
    template_name = 'games_list/tournaments_per_game.html'
        

# Create your views here.
