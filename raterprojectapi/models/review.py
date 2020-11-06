
"""Review model module"""
from django.db import models
from django.contrib.auth.models import User


class Review(models.Model):
    """Review database model"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    review = models.CharField(max_length=500)