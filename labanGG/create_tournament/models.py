from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    schedule = models.CharField(max_length=100)
    more_details = models.TextField()
    game = models.CharField(max_length=100)
    tier = models.CharField(max_length=1, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')])
    prize_pool = models.TextField()
