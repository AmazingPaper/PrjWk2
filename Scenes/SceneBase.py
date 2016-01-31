import random

import pygame


class SceneBase:
	def __init__(self, game):
		self.game = game
		self.next = self

		print("IN SCENE : {}".format(type(self).__name__))
	def ProcessInput(self, events, pressed_keys):
		print("uh-oh, you didn't override this in the child class")

	def Update(self):
		print("uh-oh, you didn't override this in the child class")

	def Render(self, screen):
		print("uh-oh, you didn't override this in the child class")

	def SwitchToScene(self, next_scene):
		self.next = next_scene

	def Terminate(self):
		self.SwitchToScene(None)

	def quitGame(self):
		pygame.quit()
		quit()

	# Ability to roll die.
	def dieRoll(self):
		number = random.randint(1, 6)
		return number
