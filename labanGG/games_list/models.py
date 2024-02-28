from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images', null = True, blank = True)

    def __str__(self):
        return '{}'.format(self.title)

# Create your models here.
