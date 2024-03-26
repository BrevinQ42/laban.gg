from django.db import models
from register.models import Account

class TournamentPlayer(models.Model):
    accountUser = models.CharField(max_length=32, default='no account')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    ign = models.CharField(max_length=64)
    age = models.IntegerField()
    country = models.CharField(max_length=64)