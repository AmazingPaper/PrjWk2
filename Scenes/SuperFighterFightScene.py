import pygame
from pygame.constants import *

from Scenes.GameScene import GameScene


class SuperFighterFightScene(GameScene):
	def __init__(self, game):
		GameScene.__init__(self, game)

		if self.game.lastDice == 0:
			self.dieRoll()

		if self.game.superFighterCard is None:
			self.game.superFighterCard = self.game.PickSuperFighterCard()

		self.cardRect = None


	def ProcessInput(self, events, pressed_keys):
		super(SuperFighterFightScene, self).ProcessInput(events, pressed_keys)

		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if self.cardRect is not None and self.cardRect.collidepoint(event.pos):
					from Scenes.SuperFighterInfoScene import SuperFighterInfoScene

					self.SwitchToScene(SuperFighterInfoScene(self.game))
			elif event.type == KEYDOWN:
					from Scenes.GameScene import GameScene

					self.SwitchToScene(GameScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		super(SuperFighterFightScene, self).Render(screen)

		if self.game.superFighterCard is not None:
			image = self.game.superFighterCard.image.convert_alpha()
			image = pygame.transform.rotozoom(image, 45, .15)
			screen.blit(image, (210, 210))

			self.cardRect = screen.blit(image, (210, 210))
