"""Game Category model module"""
from django.db import models

class GameCategory(models.Model):
    """Game Category database model"""

    game = models.ForeignKey("Game", on_delete=models.CASCADE, related_name="game_categories")
    category = models.ForeignKey("Category", on_delete=models.CASCADE, related_name="game_categories")