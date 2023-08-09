from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=255)
    workers_count = models.IntegerField(default=0)
    games_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name
