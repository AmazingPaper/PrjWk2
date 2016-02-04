from pygame.constants import *

from Board.BoardGraphics import BoardGraphics
from Board.FightType import FightType
from GraphicsHelpers import *
from Scenes.RulesScene import RulesScene
from Scenes.SceneBase import *


class GameScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_1:
					self.movePlayerNTimes(1)
				elif event.key == K_2:
					self.movePlayerNTimes(2)
				elif event.key == K_3:
					self.movePlayerNTimes(3)
				elif event.key == K_4:
					self.movePlayerNTimes(4)
				elif event.key == K_5:
					self.movePlayerNTimes(5)
				elif event.key == K_6:
					self.movePlayerNTimes(6)
				elif event.key == K_SPACE:
					self.movePlayerNTimes(self.dieRoll())

		self.ProcessButtonEvents(events)

	def movePlayerNTimes(self, n):
		from Scenes.PlayerFightScene import PlayerFightScene
		from Scenes.SuperFighterFightScene import SuperFighterFightScene
		from Scenes.OpponentSelectionScene import OpponentSelectionScene
		from Scenes.PlayerFightRollAndChooseScreen import PlayerFightRollAndChooseScreen

		self.game.lastDice = n

		fightType = self.game.MoveCurrentPlayer(self.game.lastDice)

		current_player = self.game.CurrentPlayer()

		players = current_player.otherPlayers()
		if fightType == FightType.NoFight:
			self.game.NextPlayer()
		elif fightType == FightType.SuperFighter:
			self.SwitchToScene(SuperFighterFightScene(self.game))
		elif fightType == FightType.ChoosePlayer:
			self.SwitchToScene(OpponentSelectionScene(self.game, current_player, players))
		elif fightType == FightType.Player:
			#if current_player.isAtOtherPlayersCorner():
			#	defender = current_player.tile.cornerOfPlayer
			#	self.SwitchToScene(PlayerFightScene(self.game, current_player, defender))
			#else:
			if not current_player.isAtOtherPlayersCorner():
				defender = players[0]

				self.SwitchToScene(PlayerFightScene(self.game, current_player, defender))

				#self.SwitchToScene(PlayerFightRollAndChooseScreen(self.game, defender, current_player))

	def Update(self):
		pass

	def Render(self, screen):
		super(GameScene, self).Render(screen)

		BoardGraphics(self.game.images, screen, self.game.board).draw()

		self.__drawPlayerStatistics(screen)
		self.__drawDice(screen)
		self.__drawButtons(screen)
		self.__drawSuperFighterCard(screen)
		self.__drawPlayerName(screen)

	def __drawDice(self, screen):
		if self.game.lastDice > 0:
			screen.blit(self.game.images['dice'][self.game.lastDice], (275, 450))

	def __drawPlayerStatistics(self, screen):
		rectangles = []

		for player in self.game.players:
			row, column = player.corner

			isCurrentPlayer = player == self.game.CurrentPlayer()

			from Board.PlayerStatisticsGraphics import PlayerStatisticsGraphics
			rect = PlayerStatisticsGraphics(screen, self.game.images, player, isCurrentPlayer).draw(
				(row // 10, column // 10))

			action = lambda p: (lambda: self.switchToPlayerInfoScene(p))

			rectangle = (rect, action(player), None)

			rectangles.append(rectangle)

		self.addButtons(rectangles)

	def __drawPlayerName(self, screen):
		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		textObj = smallText.render(str(self.game.CurrentPlayer().name), True, WHITE, FONT_BLUE)
		screen.blit(textObj, (230, 80))

	def __drawSuperFighterCard(self, screen):
		image = self.game.images['superfightercard'].convert_alpha()
		image = pygame.transform.rotozoom(image, 45, .15)
		self.cardRect = screen.blit(image, (210, 210))

	def __drawButtons(self, screen):
		from Scenes.IntroScene import IntroScene

		buttonRect = (
			button("MENU", 250, 650, 100, 50, DIM_YELLOW, YELLOW, screen),
			lambda: self.SwitchToScene(IntroScene(self.game)), self.selectSound)

		self.addButton(buttonRect)

		buttonRect = (button("RULES", 250, 720, 100, 50, DIM_YELLOW, YELLOW, screen),
		              lambda: self.SwitchToScene(RulesScene(self.game)), self.selectSound)
		self.addButton(buttonRect)

	def switchToPlayerInfoScene(self, player):
		from Scenes.PlayerInfoScene import PlayerInfoScene

		self.SwitchToScene(PlayerInfoScene(self.game, player))
