from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.urls import reverse

# Create your models here.

gameStatusChoices = (
    ('F', 'First Player to Move'),
    ('S', 'Second Player to Move'),
    ('W', 'First Player Wins'),
    ('L', 'Second Player Wins'),
    ('D', 'Draw'))

class GamesQuerySet (models.QuerySet):
    def gamesForUser(self, user):
            return self.filter(Q(firstPlayer = user) | Q(secondPlayer = user))

    def active(self):
        return self.filter(Q(status = 'F') | Q(status = 'S'))
    

class Game(models.Model):
    firstPlayer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "gamesFirstPlayer")
    secondPlayer = models.ForeignKey(User, on_delete = models.CASCADE, related_name = "gamesSecondPlayer")

    startTime = models.DateTimeField(auto_now_add = True)
    lastActive = models.DateTimeField(auto_now = True)
    status = models.CharField(max_length = 1, default = 'F', choices = gameStatusChoices)

    def __str__(self):
        return "{0} vs {1}".format(self.firstPlayer, self.secondPlayer)

    def get_absolute_url(self):
        return reverse('gameplay_detail', args=[self.id])
        
    objects = GamesQuerySet.as_manager()

class Move(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    comment = models.CharField(max_length = 300, blank = True)
    byFirstPlayer = models.BooleanField()

    game = models.ForeignKey(Game, on_delete = models.CASCADE)