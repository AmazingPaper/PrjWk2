from Board.GraphicsConstants import *
from Board.PlayerStatisticsGraphics import PlayerStatisticsGraphics
from GraphicsHelpers import *


class StatisticsGraphics:
	def __init__(self, screen, images, players):
		self.images, = images,
		self.screen = screen
		self.players = players

	def draw(self):
		index = 0
		for player in self.players:
			row = index // 2
			column = index % 2

			PlayerStatisticsGraphics(self.screen, self.images, player).draw((row, column))
			index += 1
