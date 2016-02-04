from GraphicsHelpers import *
from Scenes.SuperFighterFightScene import *

class OpponentSelectionScene(GameScene):
	def __init__(self, game, player, players):
		GameScene.__init__(self, game)

		self.player = player
		self.players = players

		if game.lastDice == 0:
			self.SwitchToPreviousScene()

	def ProcessInput(self, events, pressed_keys):
		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(OpponentSelectionScene, self).Render(screen)

		pygame.draw.rect(screen, SURV_BLUE, (55, 50, 500, 500))

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2("{} vs ?".format(self.player.name), largeText)
		TextRect.center = 300, 80
		screen.blit(TextSurf, TextRect)

		largeText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects2("Select your opponent", largeText)
		TextRect.center = 300, 200
		screen.blit(TextSurf, TextRect)

		self.createSelectPlayerButtons(screen, self.players)

	def createSelectPlayerButtons(self, screen, players):

		n = 0
		for player in players:
			x = 130
			y = 300
			width = 300
			height = 50

			damages = player.damages[self.game.lastDice - 1]
			action = lambda p: lambda: self.selectOpponent(p)

			#health, condition = damages[n]

			str = " {}".format(player.name)

			button = buttonText(str, x, y + n * 80, width + 65, height, DIM_YELLOW, YELLOW, screen)

			buttonRect = (button, action(player), self.selectSound)

			self.addButton(buttonRect)
			n += 1

	def selectOpponent(self, opponent):
		attacker = self.game.CurrentPlayer()

		from Scenes.PlayerFightScene import PlayerFightScene
		self.SwitchToScene(PlayerFightScene(self.game, attacker, opponent))
