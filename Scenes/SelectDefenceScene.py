from GraphicsHelpers import *
from Scenes.GameScene import GameScene


class SelectDefenceScene(GameScene):
	def __init__(self, game):
		GameScene.__init__(self, game)

		self.superFighter = game.superFighterCard.superFighter
		self.player = game.CurrentPlayer()

		if game.lastDice == 0:
			self.SwitchToPreviousScene()

	def ProcessInput(self, events, pressed_keys):
		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(SelectDefenceScene, self).Render(screen)

		pygame.draw.rect(screen, SURV_BLUE, (55, 50, 500, 500))

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2("{} vs {}".format(self.superFighter.name, self.player.name), largeText)
		TextRect.center = 300, 80
		screen.blit(TextSurf, TextRect)

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2(
			"{} will do {} damage".format(self.superFighter.name, self.superFighter.damage[self.game.lastDice - 1]), largeText)
		TextRect.center = 300, 140
		screen.blit(TextSurf, TextRect)

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2("Select your defense", largeText)
		TextRect.center = 300, 200
		screen.blit(TextSurf, TextRect)

		self.createSelectDefenseButtons(screen,)

	def createSelectDefenseButtons(self, screen):
		damages = self.player.damages[self.game.lastDice - 1]


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
		print(health, condition)
