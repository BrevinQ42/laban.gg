from django.urls import path
from .views import my_tournaments_organizer

urlpatterns = [
    path('', my_tournaments_organizer, name='my_tournaments_organizer'),
]

app_name = "my_tournaments_organizer"