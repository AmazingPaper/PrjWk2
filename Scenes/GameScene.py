from pygame.constants import *

from Board.BoardGraphics import BoardGraphics
from Board.FightType import FightType
from Board.StatisticsGraphics import StatisticsGraphics
from GraphicsHelpers import *
from Scenes.RulesScene import RulesScene
from Scenes.SceneBase import *


class GameScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)
		self.buttons = []
		self.lastDice = 0

		self.turnIndex = 0

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					self.lastDice = number

					fightType = self.game.MoveCurrentPlayer(number)

					from Scenes.PlayerFightScene import PlayerFightScene
					from Scenes.PickSuperFighterCardScene import PickSuperFighterCardScene
					from Scenes.ChoosePlayerFightScene import ChoosePlayerFightScene

					current_player = self.game.CurrentPlayer()
					if fightType == FightType.Player:
						if current_player.isAtOtherPlayersCorner():
							defender = current_player.tile.cornerOfPlayer
						else:
							defender = current_player.otherPlayers()[0]

						self.SwitchToScene(PlayerFightScene(self.game, current_player, defender))
					elif fightType == FightType.SuperFighter:
						self.SwitchToScene(PickSuperFighterCardScene(self.game, current_player))
					elif fightType == FightType.ChoosePlayer:
						self.SwitchToScene(
							ChoosePlayerFightScene(self.game, current_player, current_player.otherPlayers()))

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action, sound) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()
						sound()

	def Update(self):
		pass

	def Render(self, screen):
		from Scenes.IntroScene import IntroScene

		# The game scene is just a blank blue screen
		screen.fill(SURV_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond

		BoardGraphics(screen, self.game.board).draw()

		StatisticsGraphics(screen, self.game.images, self.game.players).draw()

		screen.blit(self.game.images['background'], (55, 55))

		if self.lastDice > 0:
			screen.blit(self.game.images['dice'][self.lastDice], (275, 275))

		self.buttons = []

		buttonRect = (
			button("MENU", 250, 630, 100, 50, DIM_YELLOW, YELLOW, screen),
			lambda: self.SwitchToScene(IntroScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)

		buttonRect = (button("RULES", 250, 700, 100, 50, DIM_YELLOW, YELLOW, screen),
					  lambda: self.SwitchToScene(RulesScene(self.game)), self.selectSound)
		self.buttons.append(buttonRect)

		smallText = pygame.font.Font('MINECRAFT.TTF', 24)
		textObj = smallText.render(str(self.game.CurrentPlayer().name), True, WHITE, BLACK)
		screen.blit(textObj, (230, 100))

