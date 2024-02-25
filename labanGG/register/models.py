from django.db import models

# Create your models here.
class Account(models.Model):
    username = models.CharField(max_length=32)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=32)
    isOrganizer = models.BooleanField(default=False)