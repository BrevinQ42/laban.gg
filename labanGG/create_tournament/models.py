from django.db import models

class Tournament(models.Model):
    name = models.CharField(max_length=100)
    game = models.CharField(max_length=100)
    tier = models.CharField(max_length=1, choices=[('S', 'S'), ('A', 'A'), ('B', 'B'), ('C', 'C')])
    location = models.CharField(max_length=100)
    format = models.CharField(max_length=100, choices=[('single_elimination', 'Single Elimination'), ('double_elimination', 'Double Elimination')])
    application_link = models.URLField()
    schedule = models.TextField()
    prize_pool = models.TextField()
    more_details = models.TextField()
    image = models.ImageField(upload_to='tournament_images', blank=True, null=True)