import pygame
from pygame.constants import *

from Scenes.GameScene import GameScene


class PickSuperFighterCardScene(GameScene):
	def __init__(self, game, attacker):
		GameScene.__init__(self, game)

		self.superFighterCard = self.game.PickSuperFighterCard()

		self.cardRect = None

		if self.game.lastDice == 0:
			self.dieRoll()

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					self.game.superFighterCard = self.game.PickSuperFighterCard()
			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				if self.cardRect is not None:
					if self.cardRect.collidepoint(event.pos):
						from Scenes.SuperFighterInfoScene import SuperFighterInfoScene

						self.SwitchToScene(SuperFighterInfoScene(self.game, self.game.CurrentPlayer()))
					# self.SwitchToScene(SuperFighterFightScene(self.game, self.game.CurrentPlayer(), self.card.superFighter))

	def Update(self):
		pass

	def Render(self, screen):
		super(PickSuperFighterCardScene, self).Render(screen)

		if self.game.superFighterCard is not None:
			image = self.game.superFighterCard.image.convert_alpha()
			image = pygame.transform.rotozoom(image, 45, .15)
			screen.blit(image, (210, 210))

			self.cardRect = screen.blit(image, (210, 210))
