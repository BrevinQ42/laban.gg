from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'game', 'tier', 'location', 'format', 'application_link', 'schedule', 'prize_pool', 'more_details', 'image']
