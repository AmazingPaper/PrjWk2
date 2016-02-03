from pygame.constants import *

from Board.BoardGraphics import BoardGraphics
from Board.FightType import FightType
from GraphicsHelpers import *
from Scenes.Resources import Images
from Scenes.RulesScene import RulesScene
from Scenes.SceneBase import *


class GameScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)
		self.buttons = []

		self.rectangles = []

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:

					self.game.lastDice = self.dieRoll()

					fightType = self.game.MoveCurrentPlayer(self.game.lastDice)

					from Scenes.PlayerFightScene import PlayerFightScene
					from Scenes.SuperFighterFightScene import SuperFighterFightScene
					from Scenes.ChoosePlayerFightScene import ChoosePlayerFightScene

					current_player = self.game.CurrentPlayer()
					if fightType == FightType.NoFight:
						self.game.NextPlayer()
					elif fightType == FightType.Player:
						if current_player.isAtOtherPlayersCorner():
							defender = current_player.tile.cornerOfPlayer
						else:
							defender = current_player.otherPlayers()[0]
						self.SwitchToScene(PlayerFightScene(self.game, current_player, defender))
					elif fightType == FightType.SuperFighter:
						self.SwitchToScene(SuperFighterFightScene(self.game))
					elif fightType == FightType.ChoosePlayer:
						self.SwitchToScene(
							ChoosePlayerFightScene(self.game, current_player, current_player.otherPlayers()))

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (rect, action, sound) in self.buttons:
					if rect.collidepoint(event.pos):
						action()
						sound()
						break

				for (rect, action) in self.rectangles:
					if rect.collidepoint(event.pos):
						pygame.event.clear(MOUSEBUTTONDOWN)
						action()
						break

	def Update(self):
		pass

	def Render(self, screen):
		super(GameScene, self).Render(screen)

		BoardGraphics(screen, self.game.board).draw()

		self.__drawPlayerStatistics(screen)
		self.__drawDice(screen)
		self.__drawButtons(screen)
		self.__drawSuperFighterCard(screen)
		self.__drawPlayerName(screen)

	def __drawDice(self, screen):
		if self.game.lastDice > 0:
			screen.blit(Images.dice[self.game.lastDice], (275, 450))

	def __drawPlayerStatistics(self, screen):
		self.rectangles = []
		for player in self.game.players:
			row, column = player.corner

			isCurrentPlayer = player == self.game.CurrentPlayer()

			from Board.PlayerStatisticsGraphics import PlayerStatisticsGraphics
			rect = PlayerStatisticsGraphics(screen, self.game.images, player, isCurrentPlayer).draw(
				(row // 10, column // 10))

			action = lambda p: (lambda: self.switchToPlayerInfoScene(p))

			rectangle = (rect, action(player))

			self.rectangles.append(rectangle)

	def __drawPlayerName(self, screen):
		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		textObj = smallText.render(str(self.game.CurrentPlayer().name), True, WHITE, FONT_BLUE)
		screen.blit(textObj, (230, 80))

	def __drawSuperFighterCard(self, screen):
		image = Images.superfightercard.convert_alpha()
		image = pygame.transform.rotozoom(image, 45, .15)
		self.cardRect = screen.blit(image, (210, 210))

	def __drawButtons(self, screen):
		from Scenes.IntroScene import IntroScene

		self.buttons = []
		buttonRect = (
			button("MENU", 250, 650, 100, 50, DIM_YELLOW, YELLOW, screen),
			lambda: self.SwitchToScene(IntroScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)
		buttonRect = (button("RULES", 250, 720, 100, 50, DIM_YELLOW, YELLOW, screen),
		              lambda: self.SwitchToScene(RulesScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)

	def switchToPlayerInfoScene(self, player):
		from Scenes.PlayerInfoScene import PlayerInfoScene

		self.SwitchToScene(PlayerInfoScene(self.game, player))
