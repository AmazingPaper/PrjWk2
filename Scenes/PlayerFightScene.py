from Scenes.GameScene import GameScene
from Scenes.MessageDialogScene import MessageDialogScene


class PlayerFightScene(GameScene):
	def __init__(self, game, attacker, defender):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.defender = defender

		if self.attacker.stamina <= 1 and self.defender.stamina <= 1:
			messageLines = ["You both do not have enough",
			                "condition to fight.",
			                "defender lost 15 health"]

			self.displayDialog(messageLines)
			self.handleBothDoNotHaveConditionCase()
		else:
			from Scenes.PlayerFightRollAndChooseScreen import PlayerFightRollAndChooseScreen

			self.SwitchToScene(PlayerFightRollAndChooseScreen(self.game, self.attacker, self.defender))

	def ProcessInput(self, events, pressed_keys):
		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerFightScene, self).Render(screen)

	def handleBothDoNotHaveConditionCase(self):
		self.game.DecreasePlayerHealth(self.defender, 15)
		if self.defender.lostGame():
			self.handlePlayerLostCase(self.defender)
		self.SwitchToScene(GameScene(self.game))
