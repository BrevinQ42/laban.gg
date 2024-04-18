from django.shortcuts import render
from .models import Notifications

def get_base_template(request):
    base_template = 'base_organizer.html' if request.user.isOrganizer else 'base_attendee.html'
    return base_template

def notifications_page(request):
    # Retrieve or create the notification settings for the current user
    notifications_page, created = Notifications.objects.get_or_create(account=request.user)

    if request.method == 'POST':
        notifications_page.notifications1 = request.POST.get('notifications1') == 'on'
        notifications_page.notifications2 = request.POST.get('notifications2') == 'on'
        notifications_page.notifications3 = request.POST.get('notifications3') == 'on'
        notifications_page.save()

    base_template = get_base_template(request)

    context = {
        'notifications_page': notifications_page,
        'base_template': base_template,
    }
    return render(request, 'notifications_page.html', context)
