from django.shortcuts import render


def index(request):
	return render(request, 'player_applications_list/index.html', {})