from django.shortcuts import render
from .models import Notifications

def notifications_page(request):
    # Retrieve or create the notification settings for the current user
    notifications_page, created = Notifications.objects.get_or_create(account=request.user)

    if request.method == 'POST':
        # Process the form submission
        notifications_page.notifications1 = request.POST.get('notifications1') == 'on'
        notifications_page.notifications2 = request.POST.get('notifications2') == 'on'
        notifications_page.notifications3 = request.POST.get('notifications3') == 'on'
        notifications_page.save()
        # You can add a success message here if needed

    context = {
        'notifications_page': notifications_page,
    }
    return render(request, 'notifications_page.html', context)
