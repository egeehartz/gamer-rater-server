"""Game model module"""
from django.db import models
from django.contrib.auth.models import User


class Game(models.Model):
    """Game database model"""

    title = models.CharField(max_length=75)
    description = models.CharField(max_length=75)
    designer = models.CharField(max_length=75)
    release_year = models.IntegerField()
    number_of_players = models.IntegerField()
    est_time = models.IntegerField()
    min_age = models.IntegerField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)