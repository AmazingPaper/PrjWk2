from Board.Enumerations import *
from Board.Board import Board
from Board.Player import Player

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


def printTilesWhichHasPlayer(tile):
	if len(tile.players) > 0:
		print("tile [{}] has {} players".format(tile, len(tile.players)))
	else:
		print("tile dont have players")


def drawTile(tile):
	print("drawing tile at {}:{}".format(tile.posX, tile.posY))
