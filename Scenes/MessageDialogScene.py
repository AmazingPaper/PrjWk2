from pygame.constants import *

from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.SceneBase import SceneBase


class MessageDialogScene(SceneBase):
	def __init__(self, game, messageLines, action = None):
		SceneBase.__init__(self, game)
		self.messageLines = messageLines
		self.action = action

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONDOWN:
				# if self.action is None:
				if True:
					self.SwitchToPreviousScene()

				break
		events.clear()

	def Update(self):
		pass

	def Render(self, screen):
		super(MessageDialogScene, self).Render(screen)

		pygame.draw.rect(screen, YELLOW, (205, 0, 195, 70))
		pygame.draw.rect(screen, YELLOW, (105, 750, 400, 80))

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 20)
		TextSurf, TextRect = text_objects1("MESSAGE", smallText)
		TextRect.center = (MapWidth * TileSize / 2, MapHeight * TileSize / 12)
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
		TextSurf, TextRect = text_objects1("PRESS ANY BUTTON TO GO BACK", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), (780))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['box_glove'], (50, 100))

		y = 200

		for message in self.messageLines:
			smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
			TextSurf, TextRect = text_objects2(message, smallText)
			TextRect.center = (MapWidth * TileSize / 2, y)
			screen.blit(TextSurf, TextRect)

			y += TextRect.height + 20


