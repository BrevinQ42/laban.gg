from django.db import models
from django.urls import reverse

class Game(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images', null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.title)

    def get_absolute_url(self):
        return reverse('games_list:games-detail', kwargs={'pk':self.pk})

# Create your models here.
