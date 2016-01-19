list = []

def PlayerCount():
    for i in range(1, 5):
        name = str(input("Player " + str(i) + " please enter your name: "))
        list.append([name])
        list.append([i + 1])

PlayerCount()

