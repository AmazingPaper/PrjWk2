from pygame.constants import *

from Board.StatisticsGraphics import *
from Scenes.GameScene import GameScene


class PlayerWinScene(GameScene):
	def __init__(self, game, winner):
		pygame.mixer.music.load("Sounds/Survivor.ogg")
		pygame.mixer.music.play()

		GameScene.__init__(self, game)
		self.winner = winner

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				from Scenes.IntroScene import IntroScene
				self.SwitchToScene(IntroScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		super(GameScene, self).Render(screen)

		pygame.draw.rect(screen, YELLOW, (160, 0, 275, 500))

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 30)
		TextSurf, TextRect = text_objects3("YOU WIN", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 30)
		TextSurf, TextRect = text_objects3(self.winner.name, smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 6))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['boxwinner'], (-70, 200))
		screen.blit(self.game.images['laurel'], (200, 160))

		pygame.draw.rect(screen, YELLOW, (-10, 750, 700, 100))

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects3("PRESS ANY KEY TO GO BACK TO MENU", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), (785))
		screen.blit(TextSurf, TextRect)
