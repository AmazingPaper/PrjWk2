import pygame

from Board.Board import Board
from Board.Enumerations import PlayerType, TileType
from Board.FightType import FightType
from Board.Player import Player


class SurvivorGame:
	def __init__(self):
		self.board = Board()
		self.players = []
		self.currentPlayer = None

		pygame.init()

		diceImages = {}

		for n in range(1, 7):
			diceImages[n] = pygame.image.load("Tiles/Roll{}.png".format(n))

		self.images = {
			'rules': pygame.image.load("images/regels v2.5.png".format(n)),
			'dice': diceImages,
			'background': pygame.image.load("Tiles/background.png"),
			'introbackground' : pygame.image.load('images/survivorstockimage.png'),
			'points' : {
				PlayerType.Red : pygame.image.load('Tiles/Lifepoints.png'),
				PlayerType.Blue : pygame.image.load('Tiles/LifepointsBlue.png'),
				PlayerType.Green : pygame.image.load('Tiles/LifepointsGreen.png'),
				PlayerType.Yellow : pygame.image.load('Tiles/LifepointsYellow.png'),
			},
			'conditionPoints' : pygame.image.load('Tiles/Conditionpoints.png'),
		}
	def Reset(self, numberOfPlayers):
		self.board = Board()
		self.__setPlayers(numberOfPlayers)

	def __setPlayers(self, numberOfPlayers):
		players = [Player(PlayerType.Blue), Player(PlayerType.Red)]

		self.board.placePlayer(players[0], 0, 0)
		self.board.placePlayer(players[1], 0, 10)

		if numberOfPlayers == 3:
			players.append(Player(PlayerType.Green))

			self.board.placePlayer(players[2], 10, 10)
		elif numberOfPlayers == 4:
			players.append(Player(PlayerType.Green))
			players.append(Player(PlayerType.Yellow))

			self.board.placePlayer(players[2], 10, 10)
			self.board.placePlayer(players[3], 10, 0)

		self.players = players

		self.currentPlayer = 0

	def CurrentPlayer(self):
		return self.players[self.currentPlayer]

	def MoveCurrentPlayer(self, n):

		player = self.CurrentPlayer()
		# player.moveTimes(n)
		fightType = self.MovePlayer(player, n)

		self.currentPlayer += 1
		self.currentPlayer %= len(self.players)

		return fightType

	def IsPlayerIsInGame(self, playerType):
		len([player for player in self.players if player.playerType == playerType]) == 1

	# move this player n times on the board
	def MovePlayer(self, player, n):

		fightType = FightType.NoFight

		# if player is not placed on board then display message
		if player.tile is None:
			return

		atOwnCorner = player.isAtOwnCorner()

		# will move n times
		for i in range(1, n + 1):
			# remove this player from old tile
			player.tile.players.remove(player)

			# move this player to new tile
			player.tile = player.tile.nextTile

			# add this player to the players list o new tile
			player.tile.players.append(player)

		# get the list of other players at new location
		others = player.otherPlayers()
		# if new tile is FIGHT, then has to fight with super fighter
		if player.tile.tileType == TileType.Fight:
			fightType = FightType.SuperFighter
		if player.isAtOwnCorner():
			player.health += 10
		# if there are other players in new position
		if len(others) > 0:
			# if there are more than 1 player, then player has to choose
			# which t fight with
			if len(others) > 1:
				fightType = FightType.ChoosePlayer
				#print("FIGHT! there are more players here, choose one of : " + ", ".join(
				#	[str(player.playerType) for player in others]))
			# there is one player at new position
			else:
				fightType = FightType.SuperFighter
# if new position is other player's corner then player has to fight with owner
		elif player.isAtOtherPlayersCorner() and self.IsPlayerIsInGame(player.tile.cornerOfPlayer):
			fightType = FightType.Player

		return fightType

	def PickSuperFighterCard(self):
		pass