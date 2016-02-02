from Board.GraphicsConstants import *
from Board.PlayerStatisticsGraphics import PlayerStatisticsGraphics
from GraphicsHelpers import *


class StatisticsGraphics:
	def __init__(self, screen, images, players, currentPlayer):
		self.images, = images,
		self.screen = screen
		self.players = players
		self.currentPlayer = currentPlayer

	def draw(self):
		for player in self.players:
			row, column = player.corner

			isCurrentPlayer = player == self.currentPlayer

			PlayerStatisticsGraphics(self.screen, self.images, player, isCurrentPlayer).draw((row // 10, column // 10))