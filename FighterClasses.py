import pygame


class Player:
    def __init__(self, name, LP, CP, position):
        self.Name = name
        self.Lifepoints = LP
        self.Conditionpoints = CP
        self.position = position

    def __str__(self):
        return "{} {} {} {}".format(self.Name, self.Lifepoints, self.Conditionpoints, self.position)






PlayerBlue = Player('Mike Tysen', 100, 15, [0,0])
