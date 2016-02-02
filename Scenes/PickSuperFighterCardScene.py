from pygame.constants import *

from Scenes.GameScene import GameScene
from Scenes.SuperFighterFightScene import SuperFighterFightScene


class PickSuperFighterCardScene(GameScene):
	def __init__(self, game, attacker):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.superfighter = None

		print("On this screen pick a card")

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					card = self.game.PickSuperFighterCard()

					self.SwitchToScene(SuperFighterFightScene(self.game, self.game.CurrentPlayer(), card.superFighter))

	def Update(self):
		pass

	def Render(self, screen):
		super(PickSuperFighterCardScene, self).Render(screen)
