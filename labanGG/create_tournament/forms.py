from django import forms
from .models import Tournament

class TournamentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['application_link'].required = False

    class Meta:
        model = Tournament
        fields = ['name', 'game', 'tier', 'location', 'format', 'application_link', 'schedule', 'prize_pool', 'more_details', 'image']
