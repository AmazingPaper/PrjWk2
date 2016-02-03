from Board.GraphicsConstants import *
from GraphicsHelpers import *


class PlayerStatisticsGraphics:
	def __init__(self, screen, images, player, isCurrentPlayer):
		self.screen = screen
		self.images, = images,
		self.player = player
		self.isCurrentPlayer = isCurrentPlayer

	def draw(self, pos):
		(row, column) = pos

		namecolor = RED

		if self.isCurrentPlayer:
			namecolor = WHITE

		font = pygame.font.Font('Minecraft.ttf', 18)

		posX = column * 430
		posY = MapHeight * TileSize + row * 115

		position = (posX + 20, posY)
		textObj = font.render(str(self.player.name), True, namecolor, FONT_BLUE)

		rect = self.screen.blit(textObj, position)

		position = (posX + 20, posY + 22)

		self.screen.blit(self.images['points'][self.player.playerType], position)
		textObj = font.render(str(self.player.health), True, WHITE, BLACK)
		self.screen.blit(textObj, position)

		position = (posX + 100, posY + 22)
		self.screen.blit(self.images['conditionPoints'], position)

		textObj = font.render(str(self.player.stamina), True, WHITE, BLACK)
		self.screen.blit(textObj, position)

		return rect