list = []


def Players():
    for i in range(1, 5):
        name = str(input("Player " + str(i) + " please enter your name: "))
        list.append([name])
        list.append([i])

Players()


for x in range(0,7,2):
    print("\nPlayer " + str(list[x]).strip("[']") + " has player number " + str(list[x+1]).strip("[]") + " and is ready to go!")
