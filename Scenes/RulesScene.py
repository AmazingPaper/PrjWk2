from pygame.constants import *

from GraphicsHelpers import SURV_BLUE
from Scenes.SceneBase import SceneBase


class RulesScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN or event.type == MOUSEBUTTONUP:
				from Scenes.GameScene import GameScene
				self.SwitchToScene(GameScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		screen.fill(SURV_BLUE)

		screen.blit(self.game.images['rules'], (40, 40))
