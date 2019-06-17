from django.db import models


# Create your models here.

class Seasons(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return self.year


class Matches(models.Model):
    year = models.ForeignKey(Seasons, on_delete=models.CASCADE)
    city = models.CharField(max_length=120)
    team1 = models.CharField(max_length=120)
    team2 = models.CharField(max_length=120)
    tossWinner = models.CharField(max_length=120)
    tossDecision = models.CharField(max_length=120)
    result = models.CharField(max_length=120)
    dlApplied = models.IntegerField()
    winner = models.CharField(max_length=120)
    winByRuns = models.IntegerField()
    winByWickets = models.IntegerField()
    playerOfTheMatch = models.CharField(max_length=120)
    venue = models.CharField(max_length=120)
    empire1 = models.CharField(max_length=120)
    empire2 = models.CharField(max_length=120)
