from django.db import models
from register.models import Account

class Notifications(models.Model):
    account = models.ForeignKey(Account, on_delete=models.CASCADE) # ForeignKey reference to account in register
    notifications1 = models.BooleanField(default=False) # Notification when a tournament joined is started. 
    notifications2 = models.BooleanField(default=False)  
    message = models.CharField(max_length=1000, blank=True, null=True)