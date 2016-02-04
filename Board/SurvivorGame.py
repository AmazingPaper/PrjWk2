import pygame

from Board.Board import Board
from Board.Enumerations import PlayerType, TileType
from Board.FightType import FightType
from Board.Player import Players
from Board.SuperFighterCard import CardDeck


class SurvivorGame:
	def __init__(self):
		self.board = Board()
		self.players = []
		self.currentPlayer = None
		self.cardDeck = CardDeck()

		self.defender = None
		self.superFighterCard = None

		self.lastDice = 0

		pygame.init()

		diceImages = {}

		for n in range(1, 7):
			diceImages[n] = pygame.image.load("Tiles/Roll{}.png".format(n))

		self.images = {
			'rules': pygame.image.load("images/regels v2.5.png".format(n)),
			'dice': diceImages,
			'background': pygame.image.load("Tiles/background.png"),
			'introbackground': pygame.image.load('images/survivorstockimage.png'),
			'box_glove': pygame.image.load('images/Lboximg.png'),
			'boxwinner': pygame.image.load('images/boxwinner.png'),
			'points': {
				PlayerType.Red: pygame.image.load('Tiles/Lifepoints.png'),
				PlayerType.Blue: pygame.image.load('Tiles/LifepointsBlue.png'),
				PlayerType.Green: pygame.image.load('Tiles/LifepointsGreen.png'),
				PlayerType.Yellow: pygame.image.load('Tiles/LifepointsYellow.png'),
			},
			'conditionPoints': pygame.image.load('Tiles/Conditionpoints.png'),
			'superfightercard': pygame.image.load('images/SuperFighterCard.png'),
		}

	def Reset(self, numberOfPlayers):
		self.board = Board()
		self.__setPlayers(numberOfPlayers)

	def __setPlayers(self, numberOfPlayers):
		players = []

		self.players = players

		self.currentPlayer = 0

		if numberOfPlayers == 2:
			players.append(Players.MikeTysen)
			players.append(Players.BadrHerl)

		elif numberOfPlayers == 3:
			players.append(Players.MikeTysen)
			players.append(Players.RockyBelboa)
			players.append(Players.BadrHerl)

		elif numberOfPlayers == 4:
			players.append(Players.MikeTysen)
			players.append(Players.RockyBelboa)
			players.append(Players.BadrHerl)
			players.append(Players.MannyPecquiao)

		for player in players:
			self.board.placePlayer(player)


	def CurrentPlayer(self):
		return self.players[self.currentPlayer]

	def MoveCurrentPlayer(self, n):

		player = self.CurrentPlayer()
		# player.moveTimes(n)
		fightType = self.MovePlayer(player, n)

		return fightType

	def NextPlayer(self):
		self.currentPlayer += 1
		self.currentPlayer %= len(self.players)

	def IsPlayerIsInGame(self, playerType):
		return len([player for player in self.players if player.playerType == playerType]) == 1

	# move this player n times on the board
	def MovePlayer(self, player, n):
		fightType = FightType.NoFight
		movesound = pygame.mixer.Sound("Sounds/MoveSound.ogg")
		pygame.mixer.Sound.play(movesound)

		# if player is not placed on board then display message
		if player.tile is None:
			return

		initiallyAtOwnCorner = player.isAtOwnCorner()
		passedThroughOwnCorner = False

		# will move n times
		for i in range(1, n + 1):
			# remove this player from old tile
			player.tile.players.remove(player)

			# move this player to new tile
			player.tile = player.tile.nextTile

			# add this player to the players list o new tile
			player.tile.players.append(player)

			if player.isAtOwnCorner():
				passedThroughOwnCorner = True

		# if new tile is FIGHT, then has to fight with super fighter
		if player.isAtOwnCorner():
			OwnCornerBell = pygame.mixer.Sound("Sounds/OwnCornerBell.ogg")
			pygame.mixer.Sound.play(OwnCornerBell)
			player.health += 10

		elif not initiallyAtOwnCorner and passedThroughOwnCorner:
			print("passed from own corner, increasing health/stamina")

			player.stamina += 10

		if player.health > 100:
			player.health = 100

		if player.stamina > 15:
			player.stamina = 15

		# get the list of other players at new location
		others = player.otherPlayers()

		# if there are other players in new position
		if player.tile.tileType == TileType.Fight:
			fightType = FightType.SuperFighter
		elif len(others) > 0:
			# if there are more than 1 player, then player has to choose
			# which t fight with
			if len(others) > 1:
				fightType = FightType.ChoosePlayer
			# print("FIGHT! there are more players here, choose one of : " + ", ".join(
			#	[str(player.playerType) for player in others]))
			# there is one player at new position
			else:
				fightType = FightType.Player
			# if new position is other player's corner then player has to fight with owner
		elif player.isAtOtherPlayersCorner():
			if self.IsPlayerIsInGame(player.tile.cornerOfPlayer):
				fightType = FightType.Player
			else:
				fightType = FightType.NoFight
				player.health -= 10

		return fightType

	def PickSuperFighterCard(self):
		return self.cardDeck.pickCard()

	def DecreasePlayerHealth(self, player, n):
		player.health -= n

	def RemovePlayerFromGame(self, player):
		self.players = [p for p in self.players if p is not player]

		if player.tile is not None:
			player.tile.players.remove(player)
