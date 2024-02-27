from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = ['name', 'location', 'schedule', 'more_details', 'game', 'tier', 'prize_pool']
