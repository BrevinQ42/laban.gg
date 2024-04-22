from django.shortcuts import render
from .models import Notifications
from create_tournament.models import Tournament
from join_tournament.models import TournamentPlayer

def get_base_template(request):
    base_template = 'base_organizer.html' if request.user.isOrganizer else 'base_attendee.html'
    return base_template

def notifications_page(request):
    # Retrieve or create the notification settings for the current user
    notifications_page, created = Notifications.objects.get_or_create(account=request.user)

    if request.method == 'POST':
        notifications_page.notifications1 = request.POST.get('notifications1') == 'on'
        notifications_page.notifications2 = request.POST.get('notifications2') == 'on'
        notifications_page.save()
    
    message = None

    # Update message based on tournament status
    if notifications_page.notifications1 == True:
        user = request.user
        user_tournaments = TournamentPlayer.objects.filter(account=user)
        ongoing_tournaments = Tournament.objects.filter(status='Ongoing', id__in=user_tournaments.values_list('tournament_id', flat=True))
        for tournament in ongoing_tournaments:
            message = f"The tournament you joined, '{tournament.name}' is now ongoing."
            break  

    base_template = get_base_template(request)

    context = {
        'notifications_page': notifications_page,
        'message': message,
        'base_template': base_template,
    }
    return render(request, 'notifications_page.html', context)
