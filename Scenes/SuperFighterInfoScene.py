import pygame
from pygame.constants import *

from Scenes.PickSuperFighterCardScene import PickSuperFighterCardScene


class SuperFighterInfoScene(PickSuperFighterCardScene):
	def __init__(self, game, attacker):
		PickSuperFighterCardScene.__init__(self, game, attacker)

		self.attacker = attacker

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				self.SwitchToScene(PickSuperFighterCardScene(self.game, self.attacker))

	def Update(self):
		pass

	def Render(self, screen):
		super(PickSuperFighterCardScene, self).Render(screen)

		image = self.game.superFighterCard.image.convert_alpha()
		image = pygame.transform.scale(image, (500, 750))
		screen.blit(image, (55, 30))
