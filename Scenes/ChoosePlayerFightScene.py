from pygame.constants import *

from Scenes.GameScene import GameScene
from Scenes.PlayerFightScene import PlayerFightScene

class ChoosePlayerFightScene(GameScene):
	def __init__(self, game, attacker, playersToChoose):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.playersToChoose = playersToChoose

		print("on this scene choose from one of players {}".format(playersToChoose))

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					self.lastDice = 0

					defender = self.playersToChoose[0]

					self.SwitchToScene(PlayerFightScene(self.game, self.game.CurrentPlayer(), defender))

		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(ChoosePlayerFightScene, self).Render(screen)

		# draw buttons to for other players