from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class GamesListView(View):
    def get(self, request):
        return render(request, 'games_list/index.html')

# Create your views here.
