import random

def sceneall():
    scall = [scene1, scene2, scene3, scene4]
    r = random.choice(scall)
    r()
    return 0

def scene1():
    print("1")
    return 0

def scene2():
    print("2")
    return 0

def scene3():
    print("3")
    return 0

def scene4():
    print("4")
    return 0
