from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.GameScene import GameScene
from Scenes.SceneBase import *


class PlayerSelectionScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action, sound) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()
						sound()

	def Update(self):
		pass

	def Render(self, screen):
		super(PlayerSelectionScene, self).Render(screen)

		pygame.draw.rect(screen, YELLOW, (20, 70, 570, 100))  # title box
		largeText = pygame.font.Font('8-BIT WONDER.TTF', 75)
		TextSurf, TextRect = text_objects1("SURVIVOR", largeText)
		TextRect.center = (((MapWidth * TileSize) / 1.95), ((MapHeight * TileSize) / 5))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("SETTINGS", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("PRESS HERE TO TURN OFF MUSIC IN GAME", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 2.5))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("HOW MANY PLAYERS DARE TO SURVIVE", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 1.3))
		screen.blit(TextSurf, TextRect)

		self.createPlayerCountImages(screen)

	def createPlayerCountImages(self, screen):
		for n in range(4, 1, -1):
			x = 250
			y = 520
			width = 100
			height = 50

			action = lambda n: (lambda: self.switchToGameScene(n))

			buttonRect = (button(str(n), x, y + (4 - n) * 100, width, height, DIM_YELLOW, YELLOW, screen), action(n),
						  self.selectSound)

			self.addButton(buttonRect)

			self.addButton(
					(button("OFF", 150, 300, 100, 50, DIM_YELLOW, YELLOW, screen), self.pauseMusic, self.selectSound))
			self.addButton(
					(button("ON", 350, 300, 100, 50, DIM_YELLOW, YELLOW, screen), self.unpauseMusic, self.selectSound))

	def switchToGameScene(self, numberOfPlayers):
		self.game.Reset(numberOfPlayers)
		self.SwitchToScene(GameScene(self.game))