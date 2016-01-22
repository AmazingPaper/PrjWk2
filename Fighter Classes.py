class Char:
    def __init__(self, name, n1, n2, n3, n4, n5, n6):
        self.name = name

        self.n1 = n1
        self.n2 = n2
        self.n3 = n3
        self.n4 = n4
        self.n5 = n5
        self.n6 = n6

    def __str__(self):
        return "This is {},\nhis damage with 1 = {},\nhis damage with 2 = {},\nhis damage with 3 = {},\nhis damage with 4 = {},\nhis damage with 5 = {},\nand his damage with 6 = {}".format(self.name, self.n1, self.n2,self.n3, self.n4, self.n5, self.n6)

class Player123:
    def __init__(self, name, LP, CP, posx, posy):
        self.Name = name
        self.Lifepoints = LP
        self.Conditionpoints = CP
        self.positionx = posx
        self.positiony = posy