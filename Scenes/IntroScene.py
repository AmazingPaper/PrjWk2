# The rest is code where you implement your game using the Scenes model

from Board.GraphicsConstants import *
from Scenes import OptionsScene
from Scenes import PlayerSelectionScene
from Scenes.GameScene import *


class IntroScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
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

		# images
		img = pygame.image.load('images/survivorstockimage.png')
		screen.blit(img, (20, 180))

		# interactive button
		# als muis tussen x vh object (250+100) en begin (250) zit en
		# muis zit tussen y vh object (400+50) en begin vh object (400)

		# button(text,x,y,w,h,ac,ic,action=None)

		self.buttons.append((button("FIGHT", 250, 600, 100, 50, RED, DIM_RED, screen), self.player_select))
		self.buttons.append((button("EXIT", 50, 700, 100, 50, GREY, DIM_GREY, screen), self.quitGame))
		self.buttons.append((button("OPTIONS", 450, 700, 100, 50, BLUE, DIM_BLUE, screen), self.options))

		pygame.display.update()

	def player_select(self):
		self.SwitchToScene(PlayerSelectionScene.PlayerSelectionScene())

	def options(self):
		self.SwitchToScene(OptionsScene.OptionsScene())
