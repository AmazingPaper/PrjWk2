import pygame

from Board.GraphicsConstants import *
from Board.SurvivorGame import SurvivorGame
from Scenes.IntroScene import IntroScene


def run_game(width, height, fps, starting_scene):
	pygame.init()
	screen = pygame.display.set_mode((width, height))
	clock = pygame.time.Clock()
	pygame.mixer.music.load('Sounds/oh_no_he_didnt.ogg')
	pygame.mixer.music.play(99)
	pygame.mixer.music.set_volume(0.2)

	active_scene = starting_scene
	while active_scene is not None:
		pressed_keys = pygame.key.get_pressed()
		# Event filtering
		filtered_events = []
		keyboardOrMouseEvent = False

		for event in pygame.event.get():
			quit_attempt = False

			keyboardOrMouseEvent = event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONDOWN

			if event.type == pygame.QUIT:
				quit_attempt = True
			elif event.type == pygame.KEYDOWN:
				alt_pressed = pressed_keys[pygame.K_LALT] or pressed_keys[pygame.K_RALT]
				if event.key == pygame.K_ESCAPE:
					quit_attempt = True
				elif event.key == pygame.K_F4 and alt_pressed:
					quit_attempt = True

			if quit_attempt:
				active_scene.Terminate()
			else:
				filtered_events.append(event)

		if active_scene.displayingDialog and keyboardOrMouseEvent:
			active_scene.closeDialog()
		else:
			active_scene.ProcessInput(filtered_events, pressed_keys)

		active_scene.Update()
		active_scene.Render(screen)

		active_scene = active_scene.next

		pygame.display.flip()
		clock.tick(fps)


game = SurvivorGame()

run_game(MapWidth * TileSize, MapHeight * TileSize + 200, 30, IntroScene(game))
