from pygame.constants import *

from Board.BoardGraphics import BoardGraphics
from Board.FightType import FightType
from Board.PlayerStatisticsGraphics import PlayerStatisticsGraphics
from GraphicsHelpers import *
from Scenes.RulesScene import RulesScene
from Scenes.SceneBase import *
from Board.SurvivorGame import *


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
		from Scenes.IntroScene import IntroScene

		# The game scene is just a blank blue screen
		screen.fill(FONT_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond

		BoardGraphics(screen, self.game.board).draw()

		# StatisticsGraphics(screen, self.game.images, self.game.players, self.game.CurrentPlayer()).draw()

		self.rectangles = []




		for player in self.game.players:
			row, column = player.corner

			isCurrentPlayer = player == self.game.CurrentPlayer()

			rect = PlayerStatisticsGraphics(screen, self.game.images, player, isCurrentPlayer).draw(
				(row // 10, column // 10))

			action = lambda p: (lambda: self.switchToPlayerInfoScene(p))

			rectangle = (rect, action(player))

			self.rectangles.append(rectangle)

		screen.blit(self.game.images['background'], (55, 55))

		if self.game.lastDice > 0:
			screen.blit(self.game.images['dice'][self.game.lastDice], (275, 450))




		self.buttons = []

		buttonRect = (
			button("MENU", 250, 630, 100, 50, DIM_YELLOW, YELLOW, screen),
			lambda: self.SwitchToScene(IntroScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)

		buttonRect = (button("RULES", 250, 700, 100, 50, DIM_YELLOW, YELLOW, screen),
		              lambda: self.SwitchToScene(RulesScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)

		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		textObj = smallText.render(str(self.game.CurrentPlayer().name), True, WHITE, FONT_BLUE)
		screen.blit(textObj, (230, 80))

	def switchToPlayerInfoScene(self, player):
		from Scenes.PlayerInfoScene import PlayerInfoScene

		self.SwitchToScene(PlayerInfoScene(self.game, player))

	def switchToPlayerDiedScene(self, player):
		from Scenes.HeDiedScene import HeDiedScene

		self.SwitchToScene(HeDiedScene)


