from Board.Enumerations import TileType


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
