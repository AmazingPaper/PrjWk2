import pygame
from pygame.constants import *

from GraphicsHelpers import *
from Scenes.GameScene import GameScene


class SuperFighterFightScene(GameScene):
	def __init__(self, game, attacker, superFighter):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.superFighter = superFighter

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					self.lastDice = number

					self.game.MoveCurrentPlayer(number)

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action, d) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		super(SuperFighterFightScene, self).Render(screen)

		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		textObj = smallText.render("vs", True, WHITE, BLACK)
		screen.blit(textObj, (280, 100))

		textObj = smallText.render(self.superFighter.name, True, WHITE, BLACK)
		screen.blit(textObj, (230, 120))
