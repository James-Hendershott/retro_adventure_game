from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from .models import GameState


# Define game scenes
SCENES = {
    'start': {
        'text': """
╔══════════════════════════════════════════════════════════════╗
║              WELCOME TO THE RETRO ADVENTURE                 ║
╚══════════════════════════════════════════════════════════════╝

You wake up in a dimly lit room. There's a strange glow 
coming from an old computer terminal in the corner.

What do you do?
        """,
        'choices': {
            'A': ('approach_terminal', 'Approach the terminal'),
            'B': ('check_door', 'Check the door'),
            'C': ('look_around', 'Look around the room'),
        }
    },
    'approach_terminal': {
        'text': """
You move closer to the glowing terminal. The screen flickers
with green text on a black background. It reads:

    > SYSTEM BOOT... COMPLETE
    > AWAITING USER INPUT...
    > WARNING: UNAUTHORIZED ACCESS DETECTED

What do you do?
        """,
        'choices': {
            'A': ('type_command', 'Type a command'),
            'B': ('back_away', 'Back away from the terminal'),
            'C': ('check_door', 'Leave and check the door'),
        }
    },
    'check_door': {
        'text': """
You approach the heavy metal door. It's locked from the outside,
but there's a keypad next to it showing: [_ _ _ _]

You need a 4-digit code to escape.
        """,
        'choices': {
            'A': ('try_code', 'Try entering a code'),
            'B': ('look_around', 'Look for clues in the room'),
            'C': ('approach_terminal', 'Check the terminal for help'),
        }
    },
    'look_around': {
        'text': """
You scan the room carefully. You notice:
- A desk with scattered papers
- An old poster on the wall with numbers: "1984"
- The glowing terminal
- A locked metal door

What catches your attention?
        """,
        'choices': {
            'A': ('check_papers', 'Examine the papers on the desk'),
            'B': ('examine_poster', 'Look at the poster more closely'),
            'C': ('approach_terminal', 'Investigate the terminal'),
        }
    },
    'type_command': {
        'text': """
You sit down and type on the keyboard. The system responds:

    > ACCESS GRANTED
    > WELCOME, USER
    > DOOR CODE: 1984
    > GOOD LUCK...

The terminal screen goes dark. You now know the door code!
        """,
        'choices': {
            'A': ('try_code', 'Go to the door and enter the code'),
            'B': ('look_around', 'Look around more before leaving'),
        }
    },
    'try_code': {
        'text': """
╔══════════════════════════════════════════════════════════════╗
║                    CONGRATULATIONS!                          ║
╚══════════════════════════════════════════════════════════════╝

You enter the code: 1-9-8-4

*BEEP* *BEEP* *CLICK*

The door unlocks! You push it open and step into the light...

                    >>> YOU WIN! <<<

              Thank you for playing!
        """,
        'choices': {
            'A': ('start', 'Play Again'),
        }
    },
    'check_papers': {
        'text': """
You shuffle through the papers. Most are blank, but one 
has scribbled notes:

    "Remember: The year it all began... 1984"

This might be useful!
        """,
        'choices': {
            'A': ('check_door', 'Try the door code'),
            'B': ('approach_terminal', 'Check the terminal'),
            'C': ('look_around', 'Keep looking around'),
        }
    },
    'examine_poster': {
        'text': """
The poster shows a retro computer setup. At the bottom,
in bold letters: "1984 - The Year Computing Changed Forever"

The numbers stand out prominently: 1984
        """,
        'choices': {
            'A': ('check_door', 'Try this as the door code'),
            'B': ('look_around', 'Continue exploring'),
        }
    },
    'back_away': {
        'text': """
You step back from the terminal, uncertain. The screen
continues to glow ominously in the corner.

What now?
        """,
        'choices': {
            'A': ('check_door', 'Check the door'),
            'B': ('look_around', 'Look around the room'),
            'C': ('approach_terminal', 'Return to the terminal'),
        }
    },
}


def get_or_create_game_state(session):
    """Get or create game state for the current session."""
    if not session.session_key:
        session.create()
    
    game_state, created = GameState.objects.get_or_create(
        session_key=session.session_key,
        defaults={'current_scene': 'start'}
    )
    return game_state


@require_http_methods(["GET", "POST"])
def game_view(request):
    """Main game view handling both display and choices."""
    game_state = get_or_create_game_state(request.session)
    
    if request.method == 'POST':
        choice = request.POST.get('choice')
        current_scene_data = SCENES.get(game_state.current_scene, SCENES['start'])
        
        if choice in current_scene_data['choices']:
            next_scene, _ = current_scene_data['choices'][choice]
            game_state.current_scene = next_scene
            
            # Track visited scenes
            if next_scene not in game_state.visited_scenes:
                game_state.visited_scenes.append(next_scene)
            
            game_state.save()
    
    # Get current scene
    scene_data = SCENES.get(game_state.current_scene, SCENES['start'])
    
    # Format choices for display
    formatted_choices = {
        label: description 
        for label, (_, description) in scene_data['choices'].items()
    }
    
    context = {
        'scene': {
            'text': scene_data['text'],
            'choices': formatted_choices,
        }
    }
    
    return render(request, 'game/index.html', context)
