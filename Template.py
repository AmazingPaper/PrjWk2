
# #This files contains little snippets of code that can be repurposed
# list = []
#
# def PlayerCount():
#         x = int(input("Please specify how many players will enter the game: "))
#         for i in range(0, x):
#             name = str(input("Please enter your name: "))
#             list.append([name])
#             list.append([i + 1])
#         if x == 2:
#                 print("Player " + str(list[0]).strip("[']") + " has player number " + str(list[1]).strip("[]") + " and is ready to go!")
#                 print("Player " + str(list[2]).strip("[']") + " has player number " + str(list[3]).strip("[]") + " and is ready to go!")
#
#         elif x == 3:
#                 print("Player " + str(list[4]).strip("[']") + " has player number " + str(list[5]).strip("[]") + " and is ready to go!")
#
#         else:
#                 print("Player " + str(list[6]).strip("[']") + " has player number " + str(list[7]).strip("[]") + " and is ready to go!")
#
#
# PlayerCount()

from cl import *


list = []

def PlayerCount():
    for i in range(1, 5):
        name = str(input("Player " + str(i) + " please enter your name: "))
        list.append([name])
        list.append([i + 1])

PlayerCount()


for i in range(0,7):
    print("Player " + str(list[i]).strip("[']") + " has player number " + str(list[i]).strip("[i]") + " and is ready to go!")
    i= i+1




