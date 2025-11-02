from django.contrib import admin
from .models import GameState


@admin.register(GameState)
class GameStateAdmin(admin.ModelAdmin):
    list_display = ('session_key', 'current_scene', 'created_at', 'updated_at')
    list_filter = ('created_at', 'updated_at')
    search_fields = ('session_key', 'current_scene')
    readonly_fields = ('created_at', 'updated_at')
