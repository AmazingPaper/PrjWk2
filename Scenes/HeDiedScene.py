from pygame.constants import *
from Board.SurvivorGame import *
from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.GameScene import GameScene


class HeDiedScene(GameScene):
	def __init__(self, game):
		GameScene.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				self.SwitchToScene(GameScene(self.game))


	def Update(self):
		pass

	def Render(self, screen):

		screen.fill(FONT_BLUE)

		# smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		# TextSurf, TextRect = text_objects2("YOU DIED!", smallText)
		# TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		# screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images("Tiles/SkullBlue.jpg"), (40, 80))

		pygame.display.update()
