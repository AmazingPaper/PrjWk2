# import enumeration from Enum
# check link https://docs.python.org/3/library/enum.html for enumerations in python
from enum import Enum


# enumeration tyoe for type of tile
class TileType(Enum):
	PlayerCorner = 1,
	Fight = 2,
	IdleBlack = 3,
	IdleWhite = 4


# enumeration type for player type
class PlayerType(Enum):
	Red = 1,
	Blue = 2,
	Green = 3,
	Yellow = 4


# tile class
# keeps information such as position, tile type and if is corner of a player
class TileNode:
	# constructor or creating a tile node
	# at specified location with posX, posY
	# with specified tile type
	# if tile is at corner, which player it belongs, if not parameter value is None by default
	def __init__(self, posX, posY, tileType, cornerOfPlayer=None):
		self.nextTile = None
		self.tileType = tileType
		self.players = []
		self.posX = posX
		self.posY = posY
		self.cornerOfPlayer = cornerOfPlayer

	# returns string representation of this tile
	def __str__(self):
		text = "{}:{} - {}".format(self.posX, self.posY, self.tileType)

		if self.tileType == TileType.PlayerCorner:
			text += " - " + str(self.cornerOfPlayer)

		return text


# board class
# this class is for the tiles that players can move ( outer nodes of pyhsical board )
class Board:
	def __init__(self):
		# keeps track of board's start node
		self.head = None
		# keeps track of board's last node
		self.tail = None

		# creates each tile at specified location
		# and which player this tile belongs if is corner tile
		self.Add(self.__createCornerTile(0, 0, PlayerType.Red))
		self.Add(self.__createCornerTile(0, 1, PlayerType.Red))
		self.Add(self.__createBlackTile(0, 2))
		self.Add(self.__createBlackTile(0, 3))
		self.Add(self.__createWhiteTile(0, 4))
		self.Add(self.__createFightTile(0, 5))
		self.Add(self.__createBlackTile(0, 6))
		self.Add(self.__createWhiteTile(0, 7))
		self.Add(self.__createBlackTile(0, 8))
		self.Add(self.__createCornerTile(0, 9, PlayerType.Blue))
		self.Add(self.__createCornerTile(0, 10, PlayerType.Blue))
		self.Add(self.__createCornerTile(1, 10, PlayerType.Blue))
		self.Add(self.__createBlackTile(2, 10))
		self.Add(self.__createWhiteTile(3, 10))
		self.Add(self.__createBlackTile(4, 10))
		self.Add(self.__createFightTile(5, 10))
		self.Add(self.__createBlackTile(6, 10))
		self.Add(self.__createWhiteTile(7, 10))
		self.Add(self.__createBlackTile(8, 10))
		self.Add(self.__createCornerTile(9, 10, PlayerType.Green))
		self.Add(self.__createCornerTile(10, 10, PlayerType.Green))
		self.Add(self.__createCornerTile(10, 9, PlayerType.Green))
		self.Add(self.__createBlackTile(10, 8))
		self.Add(self.__createWhiteTile(10, 7))
		self.Add(self.__createBlackTile(10, 6))
		self.Add(self.__createFightTile(10, 5))
		self.Add(self.__createBlackTile(10, 4))
		self.Add(self.__createWhiteTile(10, 3))
		self.Add(self.__createBlackTile(10, 2))
		self.Add(self.__createCornerTile(10, 1, PlayerType.Yellow))
		self.Add(self.__createCornerTile(10, 0, PlayerType.Yellow))
		self.Add(self.__createCornerTile(9, 0, PlayerType.Yellow))
		self.Add(self.__createBlackTile(8, 0))
		self.Add(self.__createWhiteTile(7, 0))
		self.Add(self.__createBlackTile(6, 0))
		self.Add(self.__createFightTile(5, 0))
		self.Add(self.__createBlackTile(4, 0))
		self.Add(self.__createWhiteTile(3, 0))
		self.Add(self.__createBlackTile(2, 0))
		self.Add(self.__createCornerTile(1, 0, PlayerType.Red))
		self.Add(self.head)

	# adds a new tile at the end of last tile
	def Add(self, tile):
		# if board is already empty
		if self.head is None:
			self.head = tile
			self.tail = tile
		else:
			# add tile to the last and set it as last tile
			self.tail.nextTile = tile
			self.tail = tile

		return self

	# gets tile at specified position
	def getTile(self, posX, posY):
		# start from beginning of head
		current = self.head

		# enter infinite loop
		while True:
			# if current node is specified position then return it
			if current.posX == posX and current.posY == posY:
				return current

			# move to next tile
			current = current.nextTile

			# if we returned to start, could not found
			# return None
			if current == self.head:
				return None

		# not found return Node
		return None

	# high order function to apply function to all tiles
	def Iter(self, f):
		# start with start tile ( at 0:0 )
		current = self.head

		# enter infinite loop
		while True:
			# apply function to current tile
			f(current)

			# move to next tile
			current = current.nextTile

			# if we returned to start, exit loop
			if current == self.head: break

	# places a player at specified position
	def placePlayer(self, player, posX, posY):
		# get the tile at specified position
		tile = self.getTile(posX, posY)

		# if tile is None, then invalid positon is specified, display error message
		if tile is None:
			print("Cannot place player {} at {}:{}, invalid position!".format(player, posX, posY))
		else:
			# add this player to the list of players at this tile
			tile.players.append(player)

			# if this player was placed within another tile already,
			# remove it from the players list of old tile
			if player.tile is not None:
				player.tile.players.remove(player)

			# move player to found tile
			player.tile = tile

	# creates a corner tile at specified location, and sets which user this corner belongs to
	def __createCornerTile(self, posX, posY, cornerOfPlayer):
		return TileNode(posX, posY, TileType.PlayerCorner, cornerOfPlayer)

	# cretates a white tile at specified location
	def __createWhiteTile(self, posX, posY):
		return TileNode(posX, posY, TileType.IdleWhite)

	# cretates a black tile at specified location
	def __createBlackTile(self, posX, posY):
		return TileNode(posX, posY, TileType.IdleBlack)

	# cretates a fight tile at specified location
	# if user comes here, has to fight with superfighter
	def __createFightTile(self, posX, posY):
		return TileNode(posX, posY, TileType.Fight)


# player class
# keeps information about player type (red, green, blue, yellow)
# which tile this is player currently at
class Player():
	def __init__(self, playerType):
		self.playerType = playerType
		self.tile = None

	# is this user currently at his/her corner?
	def isAtOwnCorner(self):
		# if user is not placed on board then return False
		if self.tile is None:
			return False

		# return if is at own corner
		return self.tile.tileType == TileType.PlayerCorner and self.tile.cornerOfPlayer == self.playerType

	# is this user currently at anther player's corner?
	def isAtOtherPlayersCorner(self):
		# if user is not placed on board then return False
		if self.tile is None:
			return False

		# return if is at another user's corner
		return self.tile.tileType == TileType.PlayerCorner and self.tile.cornerOfPlayer != self.playerType

	# are there other players in current tile?
	def isWithOtherPlayers(self):
		players = self.otherPlayers()
		return len(players) > 0

	# returns list of ther players in tile that this player is in
	# but not player himself/herself
	def otherPlayers(self):
		return [player for player in self.tile.players if player != self]

	# move this player n times on the board
	def moveTimes(self, n):
		# if player is not placed on board then display message
		if self.tile is None:
			print("Not placed on board, can't move")

			return

		print("player {} moving {} times".format(self, n))
		atOwnCorner = self.isAtOwnCorner()

		# will move n times
		for i in range(1, n + 1):
			# remove this player from old tile
			self.tile.players.remove(self)

			# move this player to new tile
			self.tile = self.tile.nextTile

			# add this player to the players list o new tile
			self.tile.players.append(self)

			print(str(self))

		# get the list of other players at new location
		others = self.otherPlayers()

		# if new tile is FIGHT, then has to fight with super fighter
		if self.tile.tileType == TileType.Fight:
			print("FIGHT! fight with superfighter! Choose superfighter")

		# if there are other players in new position
		if len(others) > 0:
			# if there are more than 1 player, then player has to choose
			# which t fight with
			if len(others) > 1:
				print("FIGHT! there are more players here, choose one of : " + ", ".join(
						[str(player.playerType) for player in others]))
			# there is one player at new position
			else:
				print("FIGHT! there is already one player here {}".format(others[0]))
		# if new position is other player's corner then player has to fight with owner
		elif self.isAtOtherPlayersCorner():
			print("FIGHT! moved to corner of {}".format(self.tile.cornerOfPlayer))

	# return string representation of player
	# player type and  location if is placed on board
	def __str__(self):
		if self.tile is None:
			return str(self.playerType)

		return "{} @ {}:{}".format(self.playerType, self.tile.posX, self.tile.posY)


# create a new board, will have tiles already setup
board = Board()

# create players
redPlayer = Player(PlayerType.Red)
bluePlayer = Player(PlayerType.Blue)
yellowPlayer = Player(PlayerType.Yellow)
greenPlayer = Player(PlayerType.Green)

# place players on board
board.placePlayer(redPlayer, 0, 0)
board.placePlayer(bluePlayer, 0, 6)
board.placePlayer(yellowPlayer, 0, 6)
board.placePlayer(greenPlayer, 0, 8)

# will move red player from 0, 0 to 0, 5. This location is FIGHT tile
redPlayer.moveTimes(5)

# will move red player from 0, 5 to 0, 6. blue and yellow players are at this location, FIGHT
# red player has to choose which to fight with
redPlayer.moveTimes(1)

# will move red player from 0, 6 to 0, 8. green player is at this location, FIGHT
redPlayer.moveTimes(2)

# will move red player from 0, 8 to 1, 10. this is blue player's corner, FIGHT
redPlayer.moveTimes(3)

# will move red player from 1, 10 to 2, 10. there is no player here
redPlayer.moveTimes(1)

# will move red player from 2, 10 to 5, 10. This location is FIGHT tile
redPlayer.moveTimes(3)
