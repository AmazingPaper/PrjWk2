from pygame.constants import *

from Scenes.GameScene import GameScene
from Scenes.SelectDefenceScene import SelectDefenceScene


class PlayerFightScene(GameScene):
	def __init__(self, game, attacker, defender):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.defender = defender

		print("{} is now attacking to {}".format(attacker, defender))

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					print(self.attacker)
					print(self.defender)
					number = self.dieRoll()
					self.SwitchToScene(SelectDefenceScene(self.game))
					self.lastDice = number



		self.ProcessButtonEvents(events)


	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerFightScene, self) .Render(screen)

