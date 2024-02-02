import random

def sceneall():
    scall = [scene1, scene2, scene3, scene4]
    r = random.choice(scall)
    r()
    return 0

def scene1():
    print("Oh dear, you seem to have stumbled upon a rogue orc.")
    in1 = input("Do you dare to try attack it")
    return 0

def scene2():
    print("Proceed with caution, you sense something ahead of you.")
    in1 = input("Do you wish to continue forward?")
    return 0

def scene3():
    print("'You wouldn't happen to have some spare change for an old lady?" '')
    in1 = input('"Would you?"')

    return 0

def scene4():
    print('"Hello Traveller. Care to see whats in stock"')
    in1 = input('Do you want to brwose his wares?')
    return 0
