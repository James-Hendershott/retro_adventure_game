
from django.shortcuts import render, redirect
from .scenes import SCENES


def game_view(request):
	"""
	Main game view for the retro adventure game.
	Handles GET (show scene) and POST (handle choice, update session).
	Uses Django session to track current scene.
	"""
	scene_key = request.session.get('scene', 'start')
	scene = SCENES.get(scene_key, SCENES['start'])

	if request.method == "POST":
		choice = request.POST.get('choice')
		next_scene = scene['choices'].get(choice)
		if next_scene:
			request.session['scene'] = next_scene
			return redirect('game:game_view')

	return render(request, 'game/index.html', {'scene': scene})

# Create your views here.
