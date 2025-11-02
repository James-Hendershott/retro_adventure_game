from django.db import models


class GameState(models.Model):
    """Model to store game state for each session."""
    session_key = models.CharField(max_length=40, unique=True)
    current_scene = models.CharField(max_length=100, default='start')
    inventory = models.JSONField(default=list)
    visited_scenes = models.JSONField(default=list)
    game_flags = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Game State for session {self.session_key}"

    class Meta:
        verbose_name = "Game State"
        verbose_name_plural = "Game States"
