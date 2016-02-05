import pygame
from pygame.constants import *

from Scenes.GameScene import GameScene


class SuperFighterFightScene(GameScene):
	def __init__(self, game):
		GameScene.__init__(self, game)

		superfightsound = pygame.mixer.Sound("Sounds/StartFight.ogg")
		pygame.mixer.Sound.play(superfightsound)

		voicefightsound = pygame.mixer.Sound("Sounds/VoiceFight.ogg")
		pygame.mixer.Sound.play(voicefightsound)

		if self.game.superFighterCard is None:
			from Scenes.MessageDialogScene import MessageDialogScene
			from Scenes.SelectDefenceScene import SelectDefenceScene

			self.dieRoll()

			superfightsound = pygame.mixer.Sound("Sounds/StartFight.ogg")
			pygame.mixer.Sound.play(superfightsound)

			self.game.superFighterCard = self.game.PickSuperFighterCard()

		player = game.CurrentPlayer()

		super_fighter = self.game.superFighterCard.superFighter

		self.cardRect = None
		if not self.canPlayerDefend(player):
			messageLines = ["Your condition is not good for fight",
			                "you can't fight",
			                super_fighter.name,
			                "will do {} damage to you".format(super_fighter.damage[self.game.lastDice - 1])]

			self.displayDialog(messageLines)
			self.handlePlayerCantFightCase()
		elif player.stamina <= 1:
			messageLines = ["Your condition is not good to defend",
			                "you can't fight",
			                super_fighter.name,
			                "will do {} damage to you".format(super_fighter.damage[self.game.lastDice - 1])]
			self.displayDialog(messageLines)
			self.handlePlayerCantFightCase()
		else:
			messageLines = ["You are now on a Fight tile",
			                "and you have to fight with",
			                super_fighter.name]

			self.displayDialog(messageLines)
			self.switchToDefenseSelectionScene()

	def switchToDefenseSelectionScene(self):
		from Scenes.SelectDefenceScene import SelectDefenceScene

		self.SwitchToScene(SelectDefenceScene(self.game))

	def canPlayerDefend(self, player):
		damages = player.damages[self.game.lastDice - 1]

		damages = [(health, condition) for (health, condition) in damages if abs(condition) <= player.stamina]

		return len(damages) > 0

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

		self.renderDialog(screen)

	def handlePlayerCantFightCase(self):
		player = self.game.CurrentPlayer()

		super_fighter = self.game.superFighterCard.superFighter

		superFighterDamage = super_fighter.damage[self.game.lastDice - 1]

		self.game.DecreasePlayerHealth(player, superFighterDamage)

		self.game.superFighterCard = None

		if player.lostGame():
			self.handlePlayerLostCase(player)
		else:
			self.game.NextPlayer()
			self.SwitchToScene(GameScene(self.game))
