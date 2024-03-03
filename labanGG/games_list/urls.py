from django.urls import path
from .views import GamesListView
urlpatterns = [
    path('', GamesListView.as_view(), name='index'),
]
# This might be needed, depending on your Django version
app_name = "games_list"
