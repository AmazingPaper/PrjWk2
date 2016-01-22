import pygame


class Player:
    def __init__(self, name, LP, CP, position):
        self.Name = name
        self.Lifepoints = LP
        self.Conditionpoints = CP
        self.position = position

    def __str__(self):
        return "{} {} {} {}".format(self.Name, self.Lifepoints, self.Conditionpoints, self.position)



#Player Blue Info
PlayerBlue = Player('Mike Tysen', 100, 15, [0,0])

#Player Red Info
PlayerRed = Player('Rocky Belboa', 100, 15, [10,0])

#Player Yellow Info
PlayerYellow = Player('Manny Pecquiao', 100, 15, [0,10])

#Player Green Info
PlayerGreen = Player('Badr Heri', 100, 15, [10,10])

