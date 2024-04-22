from django.db import models
from register.models import Account

class Notifications(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # ForeignKey reference to account in register
    notifications1 = models.BooleanField(default=False) # Notification when a tournament joined is started. 