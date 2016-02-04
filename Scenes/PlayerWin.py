from pygame.Game import *
from pygame.constants import *

from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes import GameScene
from Scenes.SceneBase import SceneBase


class PlayerWinScene(GameScene):
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
		pygame.mixer.stop()
		pygame.mixer.music.load("Sounds/Survivor.ogg")
		pygame.mixer.music.play()

		super(GameScene, self).Render(screen)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("YOU WIN!", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['boxwinner'], (40, 500))
