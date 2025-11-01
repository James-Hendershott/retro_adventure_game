"""
SCENES module for the retro adventure game.
Defines the static scene dictionary for the game logic.
"""

SCENES = {
    "start": {
        "text": "You are Sir Knight. The CRT monitor flickers. Do you approach the castle or the forest?",
        "choices": {
            "Go to Castle": "castle_entrance",
            "Enter Forest": "forest_path"
        }
    },
    "castle_entrance": {
        "text": "You stand before the castle gates. Main entrance or side door?",
        "choices": {
            "Main Entrance": "main_entrance",
            "Side Door": "side_entrance"
        }
    },
    "forest_path": {
        "text": "The forest is dark and full of secrets. Do you follow the path or explore off-road?",
        "choices": {
            "Follow Path": "forest_path_safe",
            "Explore Off-Road": "forest_path_danger"
        }
    },
    # ...add more scenes as needed
}
