from pygame.constants import *

from Board.BoardGraphics import BoardGraphics
from Board.FightType import FightType
from Board.GraphicsConstants import *
from GraphicsHelpers import *
from Scenes.RulesScene import RulesScene
from Scenes.SceneBase import *


class GameScene(SceneBase):
	def __init__(self, game):
		SceneBase.__init__(self, game)
		self.buttons = []
		self.lastDice = 0

		self.turnIndex = 0

	def ProcessInput(self, events, pressed_keys):
		for event in events:
			if event.type == KEYDOWN:
				if event.key == K_SPACE:
					number = self.dieRoll()

					self.lastDice = number

					fightType = self.game.MoveCurrentPlayer(number)

					from Scenes.PlayerFightScene import PlayerFightScene
					from Scenes.PickSuperFighterCardScene import PickSuperFighterCardScene
					from Scenes.ChoosePlayerFightScene import ChoosePlayerFightScene

					current_player = self.game.CurrentPlayer()
					if fightType == FightType.Player:
						if current_player.isAtOtherPlayersCorner():
							defender = current_player.tile.cornerOfPlayer
						else:
							defender = current_player.otherPlayers()[0]

						self.SwitchToScene(PlayerFightScene(self.game, current_player, defender))
					elif fightType == FightType.SuperFighter:
						self.SwitchToScene(PickSuperFighterCardScene(self.game, current_player))
					elif fightType == FightType.ChoosePlayer:
						self.SwitchToScene(
							ChoosePlayerFightScene(self.game, current_player, current_player.otherPlayers()))

			elif event.type == MOUSEBUTTONDOWN and event.button == 1:
				for (buttonRect, action) in self.buttons:
					if buttonRect.collidepoint(event.pos):
						action()

	def Update(self):
		pass

	def Render(self, screen):
		from Scenes.IntroScene import IntroScene

		# The game scene is just a blank blue screen
		screen.fill(SURV_BLUE)  # maakt achtergrond weer blauw ipv menu achtergrond

		boardGraphics = BoardGraphics(screen, self.game.board)
		boardGraphics.draw()

		for player in self.game.players:
			self.__displayPlayerInfo__(screen, player)

		screen.blit(self.game.images['background'], (55, 55))

		if self.lastDice > 0:
			screen.blit(self.game.images['dice'][self.lastDice], (275, 275))

		INVFONT = pygame.font.Font('Minecraft.ttf', 18)

		self.buttons = []

		buttonRect = (
			button("MENU", 250, 675, 100, 50, YELLOW, WHITE, screen), lambda: self.SwitchToScene(IntroScene(self.game)))
		self.buttons.append(buttonRect)

		buttonRect = (button("RULES", 250, 730, 100, 50, YELLOW, DIM_YELLOW, screen),
		              lambda: self.SwitchToScene(RulesScene(self.game)))
		self.buttons.append(buttonRect)

	def __displayPlayerInfo__(self, screen, player):
		INVFONT = pygame.font.Font('Minecraft.ttf', 18)

		screen.blit(self.game.images['points'][player.playerType], (0, MapHeight * TileSize + 20))
		textObj = INVFONT.render(str(player.health), True, WHITE, BLACK)
		screen.blit(textObj, (0, MapHeight * TileSize + 20))

	def __render__(self, screen):
		INVFONT = pygame.font.Font('Minecraft.ttf', 18)

		placePosition = 10

		for item in resourcesBlue:
			screen.blit(textures[item], (placePosition, MapHeight * TileSize + 20))
			placePosition += 30
			# add the text showing the amount in the inventory
			textObj = INVFONT.render(str(inventoryBlue[item]), True, WHITE, BLACK)
			DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 20))
			placePosition += 50

		placePosition = 450

		for item in resourcesRed:
			screen.blit(textures[item], (placePosition, MapHeight * TileSize + 20))
			placePosition += 30
			# add the text showing the amount in the inventory
			textObj = INVFONT.render(str(inventoryRed[item]), True, WHITE, BLACK)
			screen.blit(textObj, (placePosition, MapHeight * TileSize + 20))
			placePosition += 50

		placePosition = 10

		for item in resourcesYellow:
			screen.blit(textures[item], (placePosition, MapHeight * TileSize + 110))
			placePosition += 30
			# add the text showing the amount in the inventory
			textObj = INVFONT.render(str(inventoryYellow[item]), True, WHITE, BLACK)
			DISPLAYSURF.blit(textObj, (placePosition, MapHeight * TileSize + 110))
			placePosition += 50

		placePosition = 450

		for item in resourcesGreen:
			screen.blit(textures[item], (placePosition, MapHeight * TileSize + 110))
			placePosition += 30
			# add the text showing the amount in the inventory
			textObj = INVFONT.render(str(inventoryGreen[item]), True, WHITE, BLACK)
			screen.blit(textObj, (placePosition, MapHeight * TileSize + 110))
			placePosition += 50

		if PlayerBlue.Lifepoints <= 0:
			SkullBlue = pygame.image.load('Tiles/SkullBlue.jpg')
			placePosition = 10
			DISPLAYSURF.blit(SkullBlue, (placePosition, MapHeight * TileSize + 20))
