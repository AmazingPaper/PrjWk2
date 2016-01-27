from Board.Enumerations import TileType


# player class
# keeps information about player type (red, green, blue, yellow)
# which tile this is player currently at
class Player():
	def __init__(self, playerType, name=""):
		self.playerType = playerType
		self.tile = None
		self.name = name
		self.health = 100
		self.stamina = 15

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

		print("{} is moving {} times".format(self, n))
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
