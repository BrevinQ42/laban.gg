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

class GamesSearchView(ListView):
    model = Game
    template_name = 'games_list/index.html'
    
    def get_queryset(self):
        query = self.request.GET.get('q')
        return Game.objects.filter(title__icontains=query).order_by('title')
        

# Create your views here.
