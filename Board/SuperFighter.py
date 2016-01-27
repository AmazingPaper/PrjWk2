class SuperFighter:
	def __init__(self, name, damages):
		self.name = name
		self.damages = damages

	def __str__(self):
		result = "This is {}".format(self.name)
		index = 1

		for damage in self.damages:
			result += "damage with {} = {}".format(index, damage)
			index += 1

		return result


Terry_Crews = SuperFighter('Terry Crews', [10, 15, 25, 20, 15, 10])
Jason_Statham = SuperFighter('Jason Statham', [15, 17, 19, 21, 23, 26])
Wesley_Sniper = SuperFighter('Wesley Sniper', [10, 12, 14, 16, 14, 12])
Jet_Ri = SuperFighter('Jet Ri', [10, 30, 12, 25, 14, 23])
Steve_Seagal = SuperFighter('Steve Seagal', [10, 15, 12, 11, 25, 20])
Super_Merio = SuperFighter('Super Merio', [10, 10, 30, 30, 15, 15])
Vin_Dieser = SuperFighter('Vin Dieser', [20, 25, 30, 25, 20, 15])
Chack_Norris = SuperFighter('Chack Norris', [15, 28, 27, 25, 29, 30])
The_Rock = SuperFighter('The Rock', [13, 28, 30, 17, 10, 7])

James_Bond = SuperFighter('James Bond', [25, 15, 15, 7, 20, 25])
Ernold_Schwarzenegger = SuperFighter('Ernold Schwarzenegger', [25, 25, 20, 15, 15, 10])
Steve_Urkel = SuperFighter('Steve Urkel', [10, 5, 12, 11, 15, 8])
Dexter = SuperFighter('Dexter', [9, 8, 7, 15, 13, 23])
Pariz_Hilton = SuperFighter('Pariz Hilton', [12, 8, 7, 15, 13, 9])
John_Cena = SuperFighter('John Cena', [10, 6, 25, 7, 8, 11])
Aqua_man = SuperFighter('Aqua Man', [12, 15, 9, 7, 7, 13])
Jackie_Chen = SuperFighter('Jackie Chen', [12, 10, 15, 9, 10, 25])
Bruce_Lee = SuperFighter('Bruce Lee', [20, 15, 5, 7, 8, 26])
