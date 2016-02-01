# The rest is code where you implement your game using the Scenes model

from Scenes import OptionsScene
from Scenes import PlayerSelectionScene
from Scenes.GameScene import *


class IntroScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)
		self.buttons = []

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		# For the sake of brevity, the title scene is a blank red screen
		screen.fill(SURV_BLUE)

		# TOP TEXT
		pygame.draw.rect(screen, YELLOW, (20, 70, 570, 100))  # title box
		largeText = pygame.font.Font('8-BIT WONDER.TTF', 75)
		TextSurf, TextRect = text_objects("SURVIVOR", largeText)
		TextRect.center = (((MapWidth * TileSize) / 1.95), ((MapHeight * TileSize) / 5))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("MENU", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['introbackground'], (20, 180))

		self.buttons = []

		self.buttons.append((button("FIGHT", 450, 700, 100, 50, DIM_RED, RED, screen), self.switchToPlayerSelectScene))
		self.buttons.append((button("EXIT", 40, 700, 100, 50, DIM_GREY, GREY, screen), self.quitGame))

	def switchToPlayerSelectScene(self):
		self.SwitchToScene(PlayerSelectionScene.PlayerSelectionScene(self.game))

	def switchToOptionsScene(self):
		self.SwitchToScene(OptionsScene.OptionsScene(self.game))
