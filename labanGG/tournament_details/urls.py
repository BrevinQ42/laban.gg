from django.urls import path
from .views import tournament_details

urlpatterns = [
    path('', tournament_details, name='tournament_details'),
]

app_name = "tournament_details"