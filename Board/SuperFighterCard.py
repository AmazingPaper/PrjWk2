
class SuperFighterCard():
	def __init__(self, name, damage):
		self.name = name
		self.damage = damage

	def __str__(self):
		result = "This is {} ".format(self.name)
		index = 1

		for damage in self.damage:
			result += "damage with {} = {} ".format(index, damage)
			index += 1
		return result

class CardDeck:
	def __init__(self):
		self.cards = [
						SuperFighterCard('Terry Crews' , (10, 15, 25, 20, 15, 10)),
						SuperFighterCard('Jason Statham' ,(15, 17, 19, 21, 23, 26)),
						SuperFighterCard('Wesley Sniper' ,(10, 12, 14, 16, 14, 12)),
						SuperFighterCard('Jet Ri' , (10, 30, 12, 25, 14, 23)),
						SuperFighterCard('Steve Seagal' , (10, 15, 12, 11, 25, 20)),
						SuperFighterCard('Super Merio' , (10, 10, 30, 30, 15, 15)),
						SuperFighterCard('Vin Dieser' , (20, 25, 30, 25, 20, 15)),
						SuperFighterCard('Chack Norris' , (15, 28, 27, 25, 29, 30)),
						SuperFighterCard('The Rock' , (13, 28, 30, 17, 10, 7)),
						SuperFighterCard('James Bond' , (25, 15, 15, 7, 20, 25)),
						SuperFighterCard('Ernold Schwarzenegger' , (25, 25, 20, 15, 15, 10)),
						SuperFighterCard('Steve Urkel' , (10, 5, 12, 11, 15, 8)),
						SuperFighterCard('Dexter' , (9, 8, 7, 15, 13, 23)),
						SuperFighterCard('Pariz Hilton' , (12, 8, 7, 15, 13, 9)),
						SuperFighterCard('John Cena' , (10, 6, 25, 7, 8, 11)),
						SuperFighterCard('Aqua Man' , (12, 15, 9, 7, 7, 13)),
						SuperFighterCard('Jackie Chen' , (12, 10, 15, 9, 10, 25)),
						SuperFighterCard('Bruce Lee' , (20, 15, 5, 7, 8, 26))
					]
		
		self._topcardindex = 0
		
	def pickCard(self):
		card = self.cards[self._topcardindex]

		self._topcardindex += 1
		self._topcardindex %= len(self.cards)

		return card
