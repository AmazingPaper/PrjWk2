from pygame.constants import MOUSEBUTTONDOWN

from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.GameScene import GameScene
from Scenes.SceneBase import *


class PlayerSelectionScene(SceneBase):
	def __init__(self):
		SceneBase.__init__(self)
		self.buttons = []
		self.createdButtons = False

	# kulanicinin yaptigi butun olaylar, tusa basma,fare hareketi burada yaziliyor.
	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):  # cizilecek olan hersey render in icinde duruyor
		# The game scene is just a blank blue screen
		screen.fill((0, 0, 255))

		screen.fill(SURV_BLUE)

		pygame.draw.rect(screen, YELLOW, (20, 70, 570, 100))  # title box
		largeText = pygame.font.Font('8-BIT WONDER.TTF', 75)
		TextSurf, TextRect = text_objects("SURVIVOR", largeText)
		TextRect.center = (((MapWidth * TileSize) / 1.95), ((MapHeight * TileSize) / 5))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("PLAYER SELECT", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("How many players dare to survive", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 2))
		screen.blit(TextSurf, TextRect)

		self.createPlayerCountImages(screen)

		pygame.display.update()

	# ekrana sirayla butonlari koyuyor ve her botunada tiklangidinda da gamescene sahnesini aciyor
	# ve parametre larak secilen kullanici sayisini geciriyor
	def createPlayerCountImages(self, screen):
		self.buttons = []

		for n in range(4, 1, -1):
			x = 250
			y = 450
			width = 100
			height = 50

			action = lambda n: (lambda: self.switchToGameScene(n))

			buttonRect = (button(str(n), x, y + (4 - n) * 100, width, height, GREEN, GREEN, screen), action(n))

			self.buttons.append(buttonRect)

	def switchToGameScene(self, numberOfPlayers):
		self.SwitchToScene(GameScene(numberOfPlayers))

