import pygame
from pygame.constants import *

from Scenes.GameScene import GameScene


class SuperFighterFightScene(GameScene):
	def __init__(self, game):
		superfightsound = pygame.mixer.Sound("Sounds/StartFight.ogg")
		pygame.mixer.Sound.play(superfightsound)

		voicefightsound = pygame.mixer.Sound("Sounds/VoiceFight.ogg")
		pygame.mixer.Sound.play(voicefightsound)

		GameScene.__init__(self, game)

		if self.game.superFighterCard is None:
			from Scenes.MessageDialogScene import MessageDialogScene
			from Scenes.SelectDefenceScene import SelectDefenceScene

			self.dieRoll()

			self.game.superFighterCard = self.game.PickSuperFighterCard()

			player = game.CurrentPlayer()

			super_fighter = self.game.superFighterCard.superFighter

			if player.stamina == 0:
				messageLines = ["You don't have enough condition points",
				                "you can't fight",
				                super_fighter.name,
				                "will do {} damage to you".format(super_fighter.damage[self.game.lastDice])]

				self.SwitchToScene(MessageDialogScene(self.game, messageLines, self.handlePlayerCantFightCase))
			else:
				messageLines = ["You are now on a Fight tile",
				                "and you have to fight with",
				                super_fighter.name,
				                "Click card on board to choose your options"]

				self.SwitchToScene(MessageDialogScene(self.game, messageLines, self.switchToDefenseSelectionScene))

		self.cardRect = None

	def switchToDefenseSelectionScene(self):
		from Scenes.SelectDefenceScene import SelectDefenceScene

		self.SwitchToScene(SelectDefenceScene(self.game))

	def ProcessInput(self, events, pressed_keys):

		super(SuperFighterFightScene, self).ProcessInput(events, pressed_keys)

		for event in events:
			if event.type == MOUSEBUTTONDOWN and event.button == 1:
				if self.cardRect is not None and self.cardRect.collidepoint(event.pos):
					from Scenes.SelectDefenceScene import SelectDefenceScene

					self.SwitchToScene(SelectDefenceScene(self.game))
			elif event.type == KEYDOWN:
				from Scenes.GameScene import GameScene

				self.SwitchToScene(GameScene(self.game))

	def Update(self):
		pass

	def Render(self, screen):
		super(SuperFighterFightScene, self).Render(screen)

		if self.game.superFighterCard is not None:
			image = self.game.superFighterCard.image.convert_alpha()
			image = pygame.transform.rotozoom(image, 45, .15)
			screen.blit(image, (210, 210))

			self.cardRect = screen.blit(image, (210, 210))

	def handlePlayerCantFightCase(self):

		player = self.game.CurrentPlayer()

		super_fighter = self.game.superFighterCard.superFighter

		player.health -= super_fighter.damage[self.game.lastDice]

		self.game.DecreasePlayerHealth(super_fighter.damage[self.game.lastDice])

		if player.lostGame():
			self.handlePlayerLostCase()
		else:
			self.game.NextPlayer()
			self.SwitchToScene(GameScene(self.game))

	def handlePlayerLostCase(self):
		self.game.RemovePlayerFromGame(self.game.CurrentPlayer())

		from Scenes.MessageDialogScene import MessageDialogScene
		messageLines = ["You have lost!"]

		self.SwitchToScene(
			MessageDialogScene(self.game, messageLines, lambda: self.SwitchToScene(GameScene(self.game))))
