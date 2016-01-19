# class Empty:
#     def __init__(self):
#         self.IsEmpty = True
# Empty = Empty()

# class Node:
#     def __init__(self, value, number, tail):
#         self.IsEmpty = False
#         self.Value = value
#         self.PlayerNumber = number
#         self.Tail = tail
#         self.HP = 100

class Player:
        def __init__(self, name, number):
            self.HP = 100
            self.name = name
            self.number = number

        def __str__(self):
            return "{} is player {} and has {} life points ".format(self.Value, self.PlayerNumber, self.HP)