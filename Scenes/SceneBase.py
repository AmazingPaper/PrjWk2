import random

from pygame.constants import MOUSEBUTTONDOWN

from Board.GraphicsConstants import *
from GraphicsHelpers import *


class SceneBase:
	def __init__(self, game):
		self.game = game
		self.next = self
		self.previous = None
		self.buttons = []
		self.displayingDialog = False
		self.messages = []

	def ProcessInput(self, events, pressed_keys):
		print("uh-oh, you didn't override ProcessInput in the child class")

	def Update(self):
		print("uh-oh, you didn't override Update in the child class")

	def Render(self, screen):
		# The game scene is just a blank blue screen
		screen.fill(FONT_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond

		self.buttons = []

	def SwitchToScene(self, next_scene):
		if next_scene is not None:
			next_scene.previous = self
			next_scene.displayingDialog = self.displayingDialog
			next_scene.messages = self.messages

		print("Switched to SCENE : {}".format(type(next_scene).__name__))

		self.next = next_scene


	def SwitchToPreviousScene(self):
		if self.previous is not None:
			self.previous.previous = None
			self.previous.next = self.previous
			self.next = self.previous

	def ProcessButtonEvents(self, events):
		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (rect, action, sound) in self.buttons:
					if rect.collidepoint(event.pos):
						action()
						if sound is not None:
							sound()

						break

	def addButton(self, button):
		self.buttons.append(button)

	def addButtons(self, buttons):
		for button in buttons:
			self.addButton(button)

	def Terminate(self):
		self.SwitchToScene(None)

	def quitGame(self):
		pygame.quit()
		quit()

	def pauseMusic(self):
		pygame.mixer.music.pause()

	def unpauseMusic(self):
		pygame.mixer.music.unpause()

	def selectSound(self):
		selectsound = pygame.mixer.Sound("Sounds/selectsound2.ogg")
		pygame.mixer.Sound.play(selectsound)

	def displayDialog(self, messages):
		if self.displayingDialog:
			for message in messages:
				self.messages.append(message)
		else:
			self.messages = messages

		self.displayingDialog = True

	def renderDialog(self, screen):
		if self.displayingDialog:
			pygame.draw.rect(screen, SURV_BLUE, (0, 200, 620, 300))

			pygame.draw.rect(screen, YELLOW, (205, 200, 195, 70))

			smallText = pygame.font.Font('8-BIT WONDER.TTF', 20)
			TextSurf, TextRect = text_objects1("MESSAGE", smallText)
			TextRect.center = (MapWidth * TileSize / 2, MapHeight * TileSize / 12 + 200)
			screen.blit(TextSurf, TextRect)

			y = 300

			for message in self.messages:
				smallText = pygame.font.Font('8-BIT WONDER.TTF', 15)
				TextSurf, TextRect = text_objects2(message, smallText)
				TextRect.center = (MapWidth * TileSize / 2, y)
				screen.blit(TextSurf, TextRect)

				y += TextRect.height + 20

	def closeDialog(self):
		self.messages = []

		self.displayingDialog = False

	# Ability to roll die.
	def dieRoll(self):
		number = random.randint(1, 6)

		self.game.lastDice = number

		return number

	def handlePlayerLostCase(self, player):
		self.game.RemovePlayerFromGame(player)

		if len(self.game.players) == 1:
			from Scenes.PlayerWin import PlayerWinScene

			self.SwitchToScene(PlayerWinScene(self.game))
		else:
			messages = ["Player {} died".format(player.name)]
			self.displayDialog(messages)

			from Scenes.GameScene import GameScene

			self.SwitchToScene(GameScene(self.game))
