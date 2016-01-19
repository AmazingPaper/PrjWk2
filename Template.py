list = []

def PlayerCount():
    for i in range(0, 4):
        name = str(input("Player " + str(i) + " please enter your name: "))
        list.append([name])
        list.append([i + 1])

PlayerCount()


for i in range(0,7,2):
    print("Player " + str(list[i]).strip("[']") + " has player number " + str(list[i+1]).strip("[i]") + " and is ready to go!")
