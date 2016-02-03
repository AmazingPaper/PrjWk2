from pygame.constants import *

from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.SceneBase import SceneBase


class PlayerWinScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				from Scenes.GameScene import IntroScene
				self.SwitchToScene(IntroScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):

		screen.fill(SURV_BLUE)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("Player Win Screen", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['rules'], (40, 80))

		pygame.display.update()
