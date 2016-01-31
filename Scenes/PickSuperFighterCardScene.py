from pygame.constants import *

from Scenes.GameScene import GameScene
from Scenes.SuperFighterFightScene import SuperFighterFightScene

class PickSuperFighterCardScene(GameScene):
	def __init__(self, game, attacker):
		GameScene.__init__(self, game)

		self.attacker = attacker

		print("On this screen pick a card")

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					self.lastDice = number

					superfighter = self.game.PickSuperFighterCard()

					self.SwitchToScene(SuperFighterFightScene(self.game, self.game.CurrentPlayer(), superfighter))

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		super(PickSuperFighterCardScene, self).Render(screen)