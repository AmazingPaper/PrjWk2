import random

import pygame
from pygame.constants import MOUSEBUTTONDOWN

from GraphicsHelpers import FONT_BLUE


class SceneBase:
	def __init__(self, game):
		self.game = game
		self.next = self
		self.previous = None
		self.buttons = []


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

	# Ability to roll die.
	def dieRoll(self):
		number = random.randint(1, 6)

		self.game.lastDice = number

		return number
