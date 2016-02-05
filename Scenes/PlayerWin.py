from pygame.constants import *

from Board.StatisticsGraphics import *
from Scenes.GameScene import GameScene
from Scenes.IntroScene import IntroScene


class PlayerWinScene(GameScene):
	def __init__(self, game, winner):
		pygame.mixer.music.load("Sounds/Survivor.ogg")
		pygame.mixer.music.play()

		GameScene.__init__(self, game)
		self.winner = winner

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				from Scenes.GameScene import IntroScene
				self.SwitchToScene(IntroScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		super(GameScene, self).Render(screen)

		pygame.draw.rect(screen, YELLOW, (200, 0, 205, 500))

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 30)
		TextSurf, TextRect = text_objects3(self.winner.name + "YOU WIN", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['boxwinner'], (-70, 200))
