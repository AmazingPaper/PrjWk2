import pygame
from pygame.constants import *

from Scenes.GameScene import GameScene


class PlayerInfoScene(GameScene):
	def __init__(self, game, player):
		GameScene.__init__(self, game)

		self.player = player

	def ProcessInput(self, events, pressed_keys):
		super(PlayerInfoScene, self).ProcessInput(events, pressed_keys)

		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				self.SwitchToPreviousScene()

	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerInfoScene, self).Render(screen)

		image = self.player.image.convert_alpha()
		image = pygame.transform.scale(image, (600, 710))
		screen.blit(image, (2, 30))
