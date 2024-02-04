#functions
import variables
def health_func(health, maxhealth, hdif):
    health += hdif
    if health > maxhealth:
        health = maxhealth
def yesno(in1, pweapon, health,maxhealth, gold):
    while True:
        in1 == in1.lower()
        if in1 == "stats":
            print("\n",pweapon[4],"\n\tDamage: ",pweapon[0],"\n\tChance of success: ",
                pweapon[1], "\n\tDurability: ", pweapon[2], "\n\tValue: ",pweapon[3],
                "\n\nHealth: ",health, "/", maxhealth,"\nGold: ", gold)
            in1 = input("please enter another response: ")
        elif in1 in variables.y:
            return("y")
            
        elif in1 in variables.n:
            return("n")
        else:
            in1 = input("please enter another response: ")

    

    


