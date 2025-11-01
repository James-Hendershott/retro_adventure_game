from django.shortcuts import render, redirect
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

from django.views.decorators.csrf import csrf_exempt

def game_view(request):
	"""
	Main game view. Handles GET (show scene) and POST (handle choice, update session).
	Uses session to track current scene.
	"""
	scene_key = request.session.get('scene', 'start')
	scene = SCENES[scene_key]

	if request.method == "POST":
		choice = request.POST.get('choice')
		next_scene = scene['choices'].get(choice)
		if next_scene:
			request.session['scene'] = next_scene
			return redirect('game:game_view')

	return render(request, 'game/index.html', {'scene': scene})

# Create your views here.
