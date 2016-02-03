from pygame.constants import *

from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.SceneBase import SceneBase


class RulesScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				from Scenes.GameScene import GameScene
				self.SwitchToScene(GameScene(self.game))
	def Update(self):
		pass

	def Render(self, screen):

		screen.fill(SURV_BLUE)

		pygame.draw.rect(screen, YELLOW, (245, 0, 115, 70))

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 20)
		TextSurf, TextRect = text_objects("Rules", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 12)
		TextSurf, TextRect = text_objects2("GAME PAUSED", smallText)
		TextRect.center = ((100), ((MapHeight * TileSize) / 20))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 12)
		TextSurf, TextRect = text_objects2("GAME PAUSED", smallText)
		TextRect.center = ((500), ((MapHeight * TileSize) / 20))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("PRESS ANY BUTTON TO GO BACK", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), (760))
		screen.blit(TextSurf, TextRect)


		screen.blit(self.game.images['rules'], (40, 80))

		pygame.display.update()
