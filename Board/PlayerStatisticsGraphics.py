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

		namecolor = WHITE

		if self.isCurrentPlayer:
			namecolor = RED

		INVFONT = pygame.font.Font('Minecraft.ttf', 18)

		position = (column * 430 + 20, MapHeight * TileSize + row * 115)
		textObj = INVFONT.render(str(self.player.name), True, namecolor, SURV_BLUE)
		self.screen.blit(textObj, position)

		position = (column * 430 + 20, MapHeight * TileSize + row * 115 + 22)

		self.screen.blit(self.images['points'][self.player.playerType], position)
		textObj = INVFONT.render(str(self.player.health), True, WHITE, BLACK)
		self.screen.blit(textObj, position)

		position = (column * 430 + 100, MapHeight * TileSize + row * 115 + 22)
		self.screen.blit(self.images['conditionPoints'], position)
		textObj = INVFONT.render(str(self.player.stamina), True, WHITE, BLACK)
		self.screen.blit(textObj, position)
