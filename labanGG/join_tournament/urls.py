from django.urls import path
from .views import join_tournament

urlpatterns = [
    path('jointournament/', join_tournament, name='join_tournament'),
]

app_name = "join_tournament"
