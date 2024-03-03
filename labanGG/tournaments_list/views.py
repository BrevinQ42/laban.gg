from django.shortcuts import render
from django.http import HttpResponse
from django.views import View

class TournamentsListView(View):
    def get(self, request):
        return render(request, 'tournaments_list/index.html')
# Create your views here.
