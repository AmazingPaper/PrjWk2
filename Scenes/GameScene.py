from pygame.constants import *

from Board.Board import Board
from Board.BoardGraphics import BoardGraphics
from Board.Enumerations import *
from Board.Player import Player
from GraphicsHelpers import *
from Scenes.SceneBase import *


class GameScene(SceneBase):
	def __init__(self, numberOfPlayers):
		SceneBase.__init__(self)
		self.numberOfPlayers = numberOfPlayers
		self.buttons = []

		self.turnIndex = 0

		board = Board()

		players = [Player(PlayerType.Red), Player(PlayerType.Blue)]

		board.placePlayer(players[0], 0, 0)
		board.placePlayer(players[1], 0, 10)

		if numberOfPlayers == 3:
			players.append(Player(PlayerType.Green))

			board.placePlayer(players[2], 10, 10)
		elif numberOfPlayers == 4:
			players.append(Player(PlayerType.Green))
			players.append(Player(PlayerType.Yellow))

			board.placePlayer(players[2], 10, 10)
			board.placePlayer(players[3], 10, 0)

		self.players = players
		self.board = board

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					player = self.players[self.turnIndex]
					player.moveTimes(number)

					self.turnIndex += 1
					self.turnIndex %= len(self.players)

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		from Scenes.IntroScene import IntroScene
		from Scenes.PlayerSelectionScene import PlayerSelectionScene

		# The game scene is just a blank blue screen
		screen.fill(SURV_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond

		boardGraphics = BoardGraphics(screen, self.board)
		boardGraphics.draw()

		INVFONT = pygame.font.Font('Minecraft.ttf', 18)

		placePosition = 10

		buttonRect = (
		button("MENU", 250, 675, 100, 50, YELLOW, WHITE, screen), lambda: self.SwitchToScene(IntroScene()))
		self.buttons.append(buttonRect)

		buttonRect = (button("RULES", 250, 730, 100, 50, YELLOW, DIM_YELLOW, screen),
		              lambda: self.SwitchToScene(PlayerSelectionScene()))
		self.buttons.append(buttonRect)
