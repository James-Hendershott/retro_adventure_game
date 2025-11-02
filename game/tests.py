from django.test import TestCase
from django.contrib.sessions.backends.db import SessionStore
from .models import GameState
from .views import get_or_create_game_state, SCENES


class GameStateModelTest(TestCase):
    def test_game_state_creation(self):
        """Test that GameState can be created."""
        game_state = GameState.objects.create(
            session_key='test_session_123',
            current_scene='start'
        )
        self.assertEqual(game_state.session_key, 'test_session_123')
        self.assertEqual(game_state.current_scene, 'start')
        self.assertEqual(game_state.inventory, [])
        self.assertEqual(game_state.visited_scenes, [])


class GameViewTest(TestCase):
    def test_game_view_get(self):
        """Test that game view loads correctly."""
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'WELCOME TO THE RETRO ADVENTURE')

    def test_game_view_post_choice(self):
        """Test that making a choice updates the game state."""
        # First GET to create session
        self.client.get('/')
        
        # Make a choice
        response = self.client.post('/', {'choice': 'A'})
        self.assertEqual(response.status_code, 200)
        
        # Check that scene changed
        session_key = self.client.session.session_key
        game_state = GameState.objects.get(session_key=session_key)
        self.assertEqual(game_state.current_scene, 'approach_terminal')


class GameLogicTest(TestCase):
    def test_all_scenes_exist(self):
        """Test that all scene references are valid."""
        for scene_name, scene_data in SCENES.items():
            for choice_label, (next_scene, _) in scene_data['choices'].items():
                self.assertIn(
                    next_scene, 
                    SCENES, 
                    f"Scene '{scene_name}' references non-existent scene '{next_scene}'"
                )

    def test_winning_path(self):
        """Test that there's a valid path to win the game."""
        # Start -> approach terminal -> type command -> try code -> win
        self.client.get('/')
        
        # Choice A from start -> approach_terminal
        self.client.post('/', {'choice': 'A'})
        
        # Choice A from approach_terminal -> type_command
        self.client.post('/', {'choice': 'A'})
        
        # Choice A from type_command -> try_code (win)
        response = self.client.post('/', {'choice': 'A'})
        
        self.assertContains(response, 'YOU WIN!')
