class Node:
    def __init__(self, value, tail):
        self.value = value
        self.tail = tail
        self.IsEmpty = False

class Empty:
    def __init__(self):
        self.IsEmpty = True


class SuperFighter():
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


def CreateFighters():
	name = ['Terry Crews', 'Jason Statham', 'Wesley Sniper', 'Jet Ri', 'Steve Seagal', 'Super Merio', 'Vin Dieser', 'Chack Norris',
			'The Rock', 'James Bond', 'Ernold Schwarzenegger', 'Steve Urkel', 'Dexter', 'Pariz Hilton', 'John Cena', 'Aqua Man',
			'Jackie Chen', 'Bruce Lee']

	damage = [(10, 15, 25, 20, 15, 10), (15, 17, 19, 21, 23, 26), (10, 12, 14, 16, 14, 12), (10, 30, 12, 25, 14, 23),
				(10, 15, 12, 11, 25, 20), (10, 10, 30, 30, 15, 15), (20, 25, 30, 25, 20, 15), (15, 28, 27, 25, 29, 30),
				(13, 28, 30, 17, 10, 7), (25, 15, 15, 7, 20, 25), (25, 25, 20, 15, 15, 10), (10, 5, 12, 11, 15, 8),
				(9, 8, 7, 15, 13, 23), (12, 8, 7, 15, 13, 9), (10, 6, 25, 7, 8, 11), (12, 15, 9, 7, 7, 13),
				(12, 10, 15, 9, 10, 25), (20, 15, 5, 7, 8, 26)]
	List = Empty()
	for i in range(len(name)):
		List = Node(SuperFighter(name[i], damage[i]), List)
	return List


SF = CreateFighters()
print (SF.tail.value.damage[0])

def RandomEnemy():
    for i in range():
        List = List.damage
    return List.name




