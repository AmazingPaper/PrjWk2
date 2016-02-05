from GraphicsHelpers import *
from Scenes.SuperFighterFightScene import *


class PlayerFightRollAndChooseScreen(GameScene):
	def __init__(self, game, defender, currentPlayer):
		GameScene.__init__(self, game)

		self.player = game.CurrentPlayer()
		self.defender = defender
		self.currentPlayer = currentPlayer


		self.attackerDamage = None

		if game.lastDice == 0:
			self.SwitchToPreviousScene()

	def ProcessInput(self, events, pressed_keys):
		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerFightRollAndChooseScreen, self).Render(screen)

		pygame.draw.rect(screen, SURV_BLUE, (55, 50, 500, 500))
		screen.blit(self.game.images['boxpvp'], (50, 160))

		largeText = pygame.font.Font('MINECRAFT.TTF', 32)
		TextSurf, TextRect = text_objects3("{} vs {}".format(self.currentPlayer.name, self.defender.name), largeText)
		TextRect.center = 300, 80
		screen.blit(TextSurf, TextRect)

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2("{} Select Your Attack".format(self.currentPlayer.name), largeText)
		TextRect.center = 300, 150
		screen.blit(TextSurf, TextRect)

		self.createSelectDefenseButtons(screen)

	def createSelectDefenseButtons(self, screen):
		damages = self.currentPlayer.damages[self.game.lastDice - 1]

		for n in range(0, 3):
			x = 130
			y = 300
			width = 300
			height = 50

			health, condition = damages[n]

			action = lambda h, c: lambda: self.selectDefense(h, c)

			str = " Damage = {} and Condition = -{}".format(health, abs(condition))

			button = buttonText(str, x, y + n * 80, width + 65, height, DIM_YELLOW, YELLOW, screen)

			buttonRect = (button, action(health, condition), self.selectSound)

			self.addButton(buttonRect)

	def selectDefense(self, health, condition):
		if abs(condition) > self.currentPlayer.stamina:
			print("Unable to execute attack, not enough stamina")
		else:
			self.currentPlayer.stamina += condition

		if self.currentPlayer == self.defender:
			print("Attacker {} - {}".format(self.player.name, self.attackerDamage))
			print("Defender {} - {}".format(self.defender.name, (health, condition)))

			print(self.attackerDamage[0])

			if health > self.attackerDamage[0]:
				self.player.health -= (health - self.attackerDamage[0])
			if self.attackerDamage[0] > health:
				self.defender.health -= (self.attackerDamage[0] - health)
			if health == self.attackerDamage[0]:
				return None





			self.SwitchToScene(GameScene(self.game))
		else:
			nextScreen = PlayerFightRollAndChooseScreen(self.game, self.defender, self.defender)
			nextScreen.attackerDamage = (health, condition)

			self.SwitchToScene(nextScreen)
