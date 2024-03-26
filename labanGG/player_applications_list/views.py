from django.shortcuts import render

from create_tournament.models import Tournament
from register.models import Account


def index(request, id):
	tournament = Tournament.objects.get(id=id)

	context = {}
	context['default_player_icon'] = "/account_profile_images/default.png"

	keyword = ""	
	applicants = Account.objects.filter(isOrganizer=False)

	if request.method == 'POST':
		if request.POST.get('searchPlayer'):
			keyword = request.POST.get('usedKeyword')
			applicants = applicants.filter(username__contains=keyword)
		else:
			for applicant in applicants:
				if request.POST.get('acceptApp' + str(applicant.id)):
					# set application status to accepted
					
					context['message'] = applicant.username + "'s application was accepted."
					break
				elif request.POST.get('rejectApp' + str(applicant.id)):
					# set application status to rejected

					context['message'] = applicant.username + "'s application was rejected."
					break

	context['applicants'] = applicants

	return render(request, 'player_applications_list/index.html', context)