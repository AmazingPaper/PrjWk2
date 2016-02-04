class SuperFighter:
	def __init__(self, name, damage):
		self.name = name
		self.health = 100
		self.damage = damage
		self.damageImages = []
		self.image = None

	def __str__(self):
		return "{}, health : {}".format(self.name, self.health)
