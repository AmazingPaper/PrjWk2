import pygame
from pygame.constants import *

from Scenes.SuperFighterFightScene import SuperFighterFightScene


class SuperFighterInfoScene(SuperFighterFightScene):
	def __init__(self, game):
		SuperFighterFightScene.__init__(self, game)


	def ProcessInput(self, events, pressed_keys):
		#super(PickSuperFighterCardScene, self).ProcessInput(events, pressed_keys)

		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				self.SwitchToScene(SuperFighterFightScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		super(SuperFighterInfoScene, self).Render(screen)

		image = self.game.superFighterCard.image.convert_alpha()
		image = pygame.transform.scale(image, (500, 750))
		screen.blit(image, (55, 30))
