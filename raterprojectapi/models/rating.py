
"""Rating model module"""
from django.db import models
from django.contrib.auth.models import User


class Rating(models.Model):
    """Rating database model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    rating = models.IntegerField()