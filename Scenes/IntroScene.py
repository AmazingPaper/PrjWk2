# The rest is code where you implement your game using the Scenes model


from Board.GraphicsConstants import *
from Scenes import PlayerSelectionScene
from Scenes.GameScene import *


class IntroScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		self.ProcessButtonEvents(events)

	def Update(self):
		pass

	def Render(self, screen):
		super(IntroScene, self).Render(screen)

		screen.fill(SURV_BLUE)

		pygame.draw.rect(screen, YELLOW, (20, 70, 570, 100))  # title box

		# TOP TEXT
		largeText = pygame.font.Font('8-BIT WONDER.TTF', 75)
		TextSurf, TextRect = text_objects("SURVIVOR", largeText)
		TextRect.center = (((MapWidth * TileSize) / 1.95), ((MapHeight * TileSize) / 5))
		screen.blit(TextSurf, TextRect)

		smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
		TextSurf, TextRect = text_objects2("MENU", smallText)
		TextRect.center = (((MapWidth * TileSize) / 2), ((MapHeight * TileSize) / 12))
		screen.blit(TextSurf, TextRect)

		screen.blit(self.game.images['introbackground'], (20, 180))
		pygame.draw.rect(screen, YELLOW, (10, 630, 110, 300))

		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("CREATED BY: ", smallText)
		TextRect.center = 70, 650
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("DAMIEN ", smallText)
		TextRect.center = 65, 680
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("MARK ", smallText)
		TextRect.center = 65, 700
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("ALEX ", smallText)
		TextRect.center = 65, 720
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("ELIF ", smallText)
		TextRect.center = 65, 740
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 15)
		TextSurf, TextRect = text_objects3("DAVID ", smallText)
		TextRect.center = 65, 760
		screen.blit(TextSurf, TextRect)
		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		TextSurf, TextRect = text_objects(" 2016 ", smallText)
		TextRect.center = 65, 790
		screen.blit(TextSurf, TextRect)

		self.addButton((button("FIGHT", 430, 250, 100, 50, DIM_RED, RED, screen), self.switchToPlayerSelectScene,
		                     self.selectSound))
		self.addButton((button("EXIT", 50, 250, 100, 50, DIM_GREY, GREY, screen), self.quitGame, self.selectSound))

	def switchToPlayerSelectScene(self):
		self.SwitchToScene(PlayerSelectionScene.PlayerSelectionScene(self.game))
