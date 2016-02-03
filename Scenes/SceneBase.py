import random

import pygame


class SceneBase:
	def __init__(self, game):
		self.game = game
		self.next = self
		self.previous = None

		print("IN SCENE : {}".format(type(self).__name__))
	def ProcessInput(self, events, pressed_keys):
		print("uh-oh, you didn't override ProcessInput in the child class")

	def Update(self):
		print("uh-oh, you didn't override Update in the child class")

	def Render(self, screen):
		print("uh-oh, you didn't override Render in the child class")

	def SwitchToScene(self, next_scene):
		if next_scene is not None:
			next_scene.previous = self
		self.next = next_scene

	def SwitchToPreviousScene(self):
		if self.previous is not None:
			self.previous.previous = None
			self.previous.next = self.previous
			self.next = self.previous

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
