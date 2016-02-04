from pygame.constants import *

from Scenes.GameScene import GameScene


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
					number = self.dieRoll()

					self.lastDice = number

					self.game.MoveCurrentPlayer(number)

		self.ProcessButtonEvents(events)


	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerFightScene, self) .Render(screen)

