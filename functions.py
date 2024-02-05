#functions
import variables
def health_func(health, maxhealth, hdif):
    health += hdif
    if health > maxhealth:
        health = maxhealth
def yesno(in1, userWeapons, health,maxhealth, gold):
    while True:
        in1 == in1.lower()
        if in1.lower() == "stats":
            for x in userWeapons:
                print("\n",x[4],"\n\tDamage: ",x[0],"\n\tChance of success: ",
                    x[1], "\n\tDurability: ", x[2], "\n\tValue: ",x[3],
                    "\n\nHealth: ",health, "/", maxhealth,"\nGold: ", gold)
                
            in1 = input("please enter another response: ")
        elif in1 in variables.y:
            return("y")
            
        elif in1 in variables.n:
            return("n")
        
            

def weaponLim(userWeapons, buyweapon):
    if userWeapons > variables.maxweapon:
        in1  = input("You have the max amount of weapons, do tou want to (drop/sell) a weapon or leave the {buyweapon} behind")
        


    
#stats check
def statsCheck(in1, userWeapons, health,maxhealth, gold):
    if in1 == "stats":
        for x in userWeapons:
            print("\n",x[4],"\n\tDamage: ",x[0],"\n\tChance of success: ",
                x[1], "\n\tDurability: ", x[2], "\n\tValue: ",x[3],
                "\n\nHealth: ",health, "/", maxhealth,"\nGold: ", gold)
        in1 = input("please enter another response: ")

    


