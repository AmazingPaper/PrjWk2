#This files contains little snippets of code that can be repurposed

list = []

def PlayerCount():
        x = int(input("Please specify how many players will enter the game: "))
        for i in range(0, x):
            name = str(input("Please enter your name: "))
            list.append([name])
            list.append([i + 1])

PlayerCount()

print("Player " + str(list[0]) + "has player number " + str(list[1]) + "and is ready to go")


