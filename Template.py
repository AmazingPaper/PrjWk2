from cl import *

list = []

def PlayerCount():
    for i in range(1, 5):
        name = str(input("Player " + str(i) + " please enter your name: "))
        list.append([name])
        list.append([i + 1])

PlayerCount()



# print("Player " + str(list[6]).strip("[']") + " has player number " + str(list[7]).strip("[]") + " and is ready to go!")




