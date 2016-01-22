class Enemy_Char:
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

Terry_Crews = Enemy_Char('Terry Crews', 10, 15, 25, 20, 15, 10)
Jason_Statham = Enemy_Char('Jason Statham', 15, 17, 19, 21, 23, 26)
Wesley_Sniper = Enemy_Char('Wesley Sniper', 10, 12, 14, 16, 14, 12)
Jet_Ri = Enemy_Char('Jet Ri', 10, 30, 12, 25, 14, 23)
Steve_Seagal = Enemy_Char('Steve Seagal', 10, 15, 12, 11, 25, 20)
Super_Merio = Enemy_Char('Super Merio', 10, 10, 30, 30, 15, 15)
Vin_Dieser = Enemy_Char('Vin Dieser', 20, 25, 30, 25, 20, 15)
Chack_Norris = Enemy_Char('Chack Norris', 15, 28, 27, 25, 29, 30)
The_Rock = Enemy_Char('The Rock', 13, 28, 30, 17, 10, 7)


James_Bond = Enemy_Char('James Bond', 25, 15, 15, 7, 20, 25)
Ernold_Schwarzenegger = Enemy_Char('Ernold Schwarzenegger', 25, 25, 20, 15, 15, 10)
Steve_Urkel = Enemy_Char('Steve Urkel', 10, 5, 12, 11, 15, 8)
Dexter = Enemy_Char('Dexter', 9, 8, 7, 15, 13, 23)
Pariz_Hilton = Enemy_Char('Pariz Hilton', 12, 8, 7, 15, 13, 9)
John_Cena = Enemy_Char('John Cena', 10, 6, 25, 7, 8, 11)
Aqua_man = Enemy_Char('Aqua Man', 12, 15, 9, 7, 7, 13)
Jackie_Chen = Enemy_Char('Jackie Chen', 12, 10, 15, 9, 10, 25)
Bruce_Lee = Enemy_Char('Bruce Lee', 20, 15, 5, 7, 8, 26)

# print(Dexter)


class Player:
    def __init__(self, name, position):
        self.Name = name
        self.Position = position
        self.Health = 100
        self.Stamina = 15


# Decrepated Player function, in favour of node lists.
# list = []
#
#
# def Players():
#     for i in range(1, 5):
#         name = str(input("Player " + str(i) + " please enter your name: "))
#         list.append([name])
#         list.append([i])
#
# Players()
# for x in range(0,7,2):
#     print("\nPlayer " + str(list[x]).strip("[']") + " has player number " + str(list[x+1]).strip("[]") + " and is ready to go!")

