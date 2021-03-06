from pygame.constants import *

from Scenes.SceneBase import *


class OptionsScene(SceneBase):
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
		# The game scene is just a blank blue screen
		screen.fill((0, 0, 255))
