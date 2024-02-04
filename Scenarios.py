import random
import functions

def sceneall( pweapon, health,maxhealth, gold):

    scall = [scene1, scene2, scene3, scene4]
    random.shuffle(scall)

    for scene in scall:
        scene(pweapon, health,maxhealth, gold)
        
    
    return 0

def scene1(pweapon, health,maxhealth, gold):
    print("Oh dear, you seem to have stumbled upon a rogue orc.")
    in1 = input("Do you dare to try attack it?: ")
    print(functions.yesno(in1,pweapon, health,maxhealth, gold))
    return 0

def scene2(pweapon, health,maxhealth, gold):
    print("Proceed with caution, you sense something ahead of you.")
    in1 = input("Do you wish to continue forward?: ")
    print(functions.yesno(in1,pweapon, health,maxhealth, gold))
    return 0

def scene3(pweapon, health,maxhealth, gold):
    print('"Would ya happen to have some spare change for an old lady?"')
    in1 = input('"Would you?": ')
    print(functions.yesno(in1,pweapon, health,maxhealth, gold))

    return 0

def scene4(pweapon, health,maxhealth, gold):
    print('"Wreetings traveller, care to see whats in stock?"')
    in1 = input('Do you want to browse his wares?: ')
    if functions.yesno(in1,pweapon, health,maxhealth, gold) == "y":
        print(f"We have the finest goods south of Winkle\n come along and ill show you\n ")
    return 0
