from django.shortcuts import render


def index(request):
	context = {}
	keyword = ""

	if request.POST.get('searchPlayer'):
		keyword = request.POST.get('usedKeyword')

	return render(request, 'player_applications_list/index.html', context)