from django.shortcuts import render

from tournament.models import Tournament
from register.models import Account


def index(request, id):
	tournament = Tournament.objects.get(id=id)

	context = {}
	context['default_player_icon'] = "/account_profile_images/default.png"

	keyword = ""

	if request.POST.get('searchPlayer'):
		keyword = request.POST.get('usedKeyword')
		applicants = Account.objects.filter(username__contains=keyword)
	else:
		applicants = Account.objects.all()

	context['applicants'] = applicants

	return render(request, 'player_applications_list/index.html', context)