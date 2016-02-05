from Board.Enumerations import *
from Board.TileNode import *


class Corners:
	TopLeft = (0, 0)
	TopRight = (0, 10)
	BottomRight = (10, 10)
	BottomLeft = (10, 0)


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
		self.Add(self.__createCornerTile(0, 0, PlayerType.Blue))
		self.Add(self.__createCornerTile(0, 1, PlayerType.Blue))
		self.Add(self.__createBlackTile(0, 2))
		self.Add(self.__createWhiteTile(0, 3))
		self.Add(self.__createBlackTile(0, 4))
		self.Add(self.__createFightTile(0, 5))
		self.Add(self.__createBlackTile(0, 6))
		self.Add(self.__createWhiteTile(0, 7))
		self.Add(self.__createBlackTile(0, 8))
		self.Add(self.__createCornerTile(0, 9, PlayerType.Red))
		self.Add(self.__createCornerTile(0, 10, PlayerType.Red))
		self.Add(self.__createCornerTile(1, 10, PlayerType.Red))
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
		self.Add(self.__createCornerTile(1, 0, PlayerType.Blue))
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
	def placePlayer(self, player):
		posX, posY = player.corner

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
			if player.tile is not None and player in player.tile.players:
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
