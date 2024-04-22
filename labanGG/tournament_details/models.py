from django.db import models
from create_tournament.models import Tournament
from join_tournament.models import TournamentPlayer


class Bracket(models.Model):
	tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
	classification = models.CharField(max_length=15)


class Matchup(models.Model):
	bracket = models.ForeignKey(Bracket, on_delete=models.CASCADE, related_name='matchups')
	matchNumber = models.IntegerField()


class PlayerInMatchup(models.Model):
	player = models.ForeignKey(TournamentPlayer, on_delete=models.CASCADE)
	matchup = models.ForeignKey(Matchup, on_delete=models.CASCADE)
	playerNumber = models.IntegerField()
