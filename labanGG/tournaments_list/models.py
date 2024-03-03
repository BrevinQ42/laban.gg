from django.db import models
#from games_list import models as games_models
import datetime

FORMAT_CHOICES = (
    ('se', 'Single Elimination'),
    ('de', 'Double Elimination')
)

class Tournament(models.Model):
    game = models.ForeignKey("games_list.Game", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to = 'images', null = True, blank = True)
    dateStart = models.DateTimeField(default = datetime.datetime.now)
    dateEnd = models.DateTimeField(default = datetime.datetime.now)
    location = models.CharField(max_length=100)
    tournyFormat = models.CharField(max_length=100, choices=FORMAT_CHOICES, default = 'se')
    details = models.TextField()
    prizePool = models.TextField(null = True)

    def __str__(self):
        return '{}'.format(self.title)
