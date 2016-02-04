import pygame
import random

from Board.SuperFighter import SuperFighter


class SuperFighterCard():
	def __init__(self, superFighter):
		self.superFighter = superFighter

		imageName = superFighter.name.replace(' ', '')

		self.image = pygame.image.load("images/SuperFighters/{}.png".format(imageName))
		self.rotatedImage = pygame.transform.rotate(self.image, 45)

	def __str__(self):
		result = "This is {} ".format(self.superFighter.name)
		index = 1

		for damage in self.damage:
			result += "damage with {} = {} ".format(index, damage)
			index += 1
		return result


class SuperFighters:
	TerryCrews = SuperFighter('Terry Crews', [10, 15, 25, 20, 15, 10])
	JasonStatham = SuperFighter('Jason Statham', [15, 17, 19, 21, 23, 26])
	WesleySniper = SuperFighter('Wesley Sniper', [10, 12, 14, 16, 14, 12])
	JetRi = SuperFighter('Jet Ri', [10, 30, 12, 25, 14, 23])
	SteveSeagal = SuperFighter('Steve Seagal', [10, 15, 12, 11, 25, 20])
	SuperMerio = SuperFighter('Super Merio', [10, 10, 30, 30, 15, 15])
	VinDieser = SuperFighter('Vin Dieser', [20, 25, 30, 25, 20, 15])
	ChackNorris = SuperFighter('Chack Norris', [15, 28, 27, 25, 29, 30])
	TheRoch = SuperFighter('The Roch', [13, 28, 30, 17, 10, 7])
	JamesBend = SuperFighter('James Bend', [25, 15, 15, 7, 20, 25])
	ErnoldSchwarzenegger = SuperFighter('Ernold Schwarzenegger', [25, 25, 20, 15, 15, 10])
	SteveUrkel = SuperFighter('Steve Urkel', [10, 5, 12, 11, 15, 8])
	Dexter = SuperFighter('Dexter', [9, 8, 7, 15, 13, 23])
	ParizHilten = SuperFighter('Pariz Hilten', [12, 8, 7, 15, 13, 9])
	JohnCena = SuperFighter('John Cena', [10, 6, 25, 7, 8, 11])
	AguaMan = SuperFighter('Agua Man', [12, 15, 9, 7, 7, 13])
	JackieChen = SuperFighter('Jackie Chen', [12, 10, 15, 9, 10, 25])
	BruceHee = SuperFighter('Bruce Hee', [20, 15, 5, 7, 8, 26])


class CardDeck:
	def __init__(self):
		self.cards = [
			SuperFighterCard(SuperFighters.TerryCrews),
			SuperFighterCard(SuperFighters.JasonStatham),
			SuperFighterCard(SuperFighters.WesleySniper),
			SuperFighterCard(SuperFighters.JetRi),
			SuperFighterCard(SuperFighters.SteveSeagal),
			SuperFighterCard(SuperFighters.SuperMerio),
			SuperFighterCard(SuperFighters.VinDieser),
			SuperFighterCard(SuperFighters.ChackNorris),
			SuperFighterCard(SuperFighters.TheRoch),
			SuperFighterCard(SuperFighters.JamesBend),
			SuperFighterCard(SuperFighters.ErnoldSchwarzenegger),
			SuperFighterCard(SuperFighters.SteveUrkel),
			SuperFighterCard(SuperFighters.Dexter),
			SuperFighterCard(SuperFighters.ParizHilten),
			SuperFighterCard(SuperFighters.JohnCena),
			SuperFighterCard(SuperFighters.AguaMan),
			SuperFighterCard(SuperFighters.JackieChen),
			SuperFighterCard(SuperFighters.BruceHee)
		]

		self._topcardindex = random.randint(0, 17)

	def pickCard(self):
		card = self.cards[self._topcardindex]

		self._topcardindex = random.randint(0, 17)
		self._topcardindex %= len(self.cards)

		return card
