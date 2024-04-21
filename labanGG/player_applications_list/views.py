from django.shortcuts import render

from create_tournament.models import Tournament
from join_tournament.models import TournamentPlayer


def index(request, id):
	tournament = Tournament.objects.get(id=id)
	
	context = {}
	context['tournament'] = tournament

	context['default_player_icon'] = "/account_profile_images/default.png"

	keyword = ""
	applicants = TournamentPlayer.objects.filter(tournament=tournament)

	if request.method == 'POST':
		if request.POST.get('searchPlayer'):
			keyword = request.POST.get('usedKeyword')
			applicants = applicants.filter(ign__contains=keyword)
		else:
			for applicant in applicants:
				if request.POST.get('acceptApp' + str(applicant.id)):
					applicant = TournamentPlayer.objects.get(id=applicant.id)
					applicant.application_status = "Accepted"
					applicant.save()
					
					context['message'] = applicant.ign + "'s application was accepted."
					break
				elif request.POST.get('rejectApp' + str(applicant.id)):
					applicant = TournamentPlayer.objects.get(id=applicant.id)
					applicant.application_status = "Rejected"
					applicant.save()

					context['message'] = applicant.ign + "'s application was rejected."
					break

	applicants = applicants.filter(application_status="Pending")

	context['applicants'] = applicants

	return render(request, 'player_applications_list/index.html', context)