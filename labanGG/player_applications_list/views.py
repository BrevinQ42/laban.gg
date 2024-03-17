from django.shortcuts import render

from register.models import Account


def index(request):
	context = {}
	context['default_player_icon'] = "/account_profile_images/default.png"

	keyword = ""

	if request.POST.get('searchPlayer'):
		keyword = request.POST.get('usedKeyword')
	context['applicants'] = Account.objects.all()

	return render(request, 'player_applications_list/index.html', context)