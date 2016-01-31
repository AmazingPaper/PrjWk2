from pygame.constants import *

from Scenes.GameScene import GameScene


class SuperFighterFightScene(GameScene):
	def __init__(self, game, attacker, superFighter):
		GameScene.__init__(self, game)

		self.attacker = attacker
		self.superFighter = superFighter

		print("on this screen fight with {}".format(superFighter))

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					self.lastDice = number

					self.game.MoveCurrentPlayer(number)

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		super(SuperFighterFightScene, self).Render(screen)