import pygame
import random

class SuperFighter:
	def __init__(self, name):
		self.name = name
		self.health = 100

	def __str__(self):
		return "{}, health : {}".format(self.name, self.health)


class SuperFighterCard():
	def __init__(self, superFighter, damage):
		self.superFighter = superFighter
		self.damage = damage

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
	TerryCrews = SuperFighter('Terry Crews')
	JasonStatham = SuperFighter('Jason Statham')
	WesleySniper = SuperFighter('Wesley Sniper')
	JetRi = SuperFighter('Jet Ri')
	SteveSeagal = SuperFighter('Steve Seagal')
	SuperMerio = SuperFighter('Super Merio')
	VinDieser = SuperFighter('Vin Dieser')
	ChackNorris = SuperFighter('Chack Norris')
	TheRoch = SuperFighter('The Roch')
	JamesBend = SuperFighter('James Bend')
	ErnoldSchwarzenegger = SuperFighter('Ernold Schwarzenegger')
	SteveUrkel = SuperFighter('Steve Urkel')
	Dexter = SuperFighter('Dexter')
	ParizHilten = SuperFighter('Pariz Hilten')
	JohnCena = SuperFighter('John Cena')
	AguaMan = SuperFighter('Agua Man')
	JackieChen = SuperFighter('Jackie Chen')
	BruceHee = SuperFighter('Bruce Hee')


class CardDeck:
	def __init__(self):
		self.cards = [
			SuperFighterCard(SuperFighters.TerryCrews, (10, 15, 25, 20, 15, 10)),
			SuperFighterCard(SuperFighters.JasonStatham, (15, 17, 19, 21, 23, 26)),
			SuperFighterCard(SuperFighters.WesleySniper, (10, 12, 14, 16, 14, 12)),
			SuperFighterCard(SuperFighters.JetRi, (10, 30, 12, 25, 14, 23)),
			SuperFighterCard(SuperFighters.SteveSeagal, (10, 15, 12, 11, 25, 20)),
			SuperFighterCard(SuperFighters.SuperMerio, (10, 10, 30, 30, 15, 15)),
			SuperFighterCard(SuperFighters.VinDieser, (20, 25, 30, 25, 20, 15)),
			SuperFighterCard(SuperFighters.ChackNorris, (15, 28, 27, 25, 29, 30)),
			SuperFighterCard(SuperFighters.TheRoch, (13, 28, 30, 17, 10, 7)),
			SuperFighterCard(SuperFighters.JamesBend, (25, 15, 15, 7, 20, 25)),
			SuperFighterCard(SuperFighters.ErnoldSchwarzenegger, (25, 25, 20, 15, 15, 10)),
			SuperFighterCard(SuperFighters.SteveUrkel, (10, 5, 12, 11, 15, 8)),
			SuperFighterCard(SuperFighters.Dexter, (9, 8, 7, 15, 13, 23)),
			SuperFighterCard(SuperFighters.ParizHilten, (12, 8, 7, 15, 13, 9)),
			SuperFighterCard(SuperFighters.JohnCena, (10, 6, 25, 7, 8, 11)),
			SuperFighterCard(SuperFighters.AguaMan, (12, 15, 9, 7, 7, 13)),
			SuperFighterCard(SuperFighters.JackieChen, (12, 10, 15, 9, 10, 25)),
			SuperFighterCard(SuperFighters.BruceHee, (20, 15, 5, 7, 8, 26))
		]

		self._topcardindex = random.randint(0, 17)

	def pickCard(self):
		card = self.cards[self._topcardindex]

		self._topcardindex = random.randint(0, 17)
		self._topcardindex %= len(self.cards)

		return card
