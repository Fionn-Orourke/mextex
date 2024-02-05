
import random
import functions
import variables

def sceneall(userWeapons, health,maxhealth, gold):

    scall = [scene1, scene2, scene3, scene4]
    random.shuffle(scall)

    for scene in scall:
        scene(userWeapons, health, maxhealth, gold)
        
    
    return 0

def scene1(userWeapons, health,maxhealth, gold):
    print("Oh dear, you seem to have stumbled upon a rogue orc.")
    in1 = input("Do you dare to try attack it?: ")
    functions.yesno(in1, userWeapons, health,maxhealth, gold)
    print(functions.yesno(in1,userWeapons, health,maxhealth, gold))
    return 0

def scene2(userWeapons, health,maxhealth, gold):
    print("Proceed with caution, you sense something ahead of you.")
    in1 = input("Do you wish to continue forward?: ")
    print(functions.yesno(in1,userWeapons, health,maxhealth, gold))
    return 0

def scene3(userWeapons, health,maxhealth, gold):
    print('"Would ya happen to have some spare change for an old lady?"')
    in1 = input('"Would you?": ')
    print(functions.yesno(in1,userWeapons, health,maxhealth, gold))

    return 0

def scene4(userWeapons, health,maxhealth, gold):
    print('"Greetings traveller, care to see whats in stock?"')
    sweapons = [variables.lonngSword, variables.club]
    in1 = input('Do you want to browse his wares?: ')
    if functions.yesno(in1,userWeapons, health,maxhealth, gold) == "y":
        print(f"We have the finest goods south of Winkle.\n Come along and ill show you.\n ")
        in1 = input("Are you intrested in food or battleware.")
        if functions.yesno(in1,userWeapons, health,maxhealth, gold)== "y":
            n = 0
            for x in sweapons:
                n += 1
                stats = x
                print ("\n",n,".",stats[4],"\n\tDamage: ",stats[0],"\n\tChance of success: ", stats[1], "\n\tDurability: ", stats[2], "\n\tValue: ",stats[3])
            in1 = input("Do you want to buy one")
            if functions.yesno(in1 ,userWeapons, health,maxhealth, gold) == "y":
                in1 = input("Which one?").lower()
                print(".lower working")
                functions.statsCheck(in1, userWeapons, health,maxhealth, gold)
                n=0
                g = 0
                
                for x in sweapons:
                    

                    if in1 != x[n]:
                        g +=1
                    
                    if in1.lower == x[4].lower() or (f"{n+1}"):
                        variables.userWeapons += x


                        print(f"Ah the {x[4]}, a worthy choice")
                        in1 = input("ff:")
                        functions.statsCheck(in1, userWeapons, health,maxhealth, gold)
                        n+=1
                    elif g == 2:
                        in1 = input("please enter a valid response")

                    n+=1
            else:
                print("the food section is just over here")

    return 0

