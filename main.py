import functions
import Scenarios
import variables
mace = variables.mace
sword = variables.sword
dagger = variables.dagger
health = variables.health
maxhealth = variables.maxhealth
gold = variables.gold
#weapon order (damage, chance of success(%),durability, value )

ap = 0
maxhealth = 100
gold = 20
ehealth = 10
#pfight = [pdamage

sweapons = ["Dagger", "Sword", "Mace"]
sweapon_stats = [dagger, sword, mace]
for x in sweapons:
    if x == sweapons[0]:
        stats = dagger
    if x == sweapons[1]:
        stats = sword
    if x == sweapons[2]:
        stats = mace
    print ("\n",x,"\n\tDamage: ",stats[0],"\n\tChance of success: ", stats[1], "\n\tDurability: ", stats[2], "\n\tValue: ",stats[3])
print (f"Choose your weapon (1.{sweapons[0]}  2.{sweapons[1]}  3.{sweapons[2]})")
in1 = int(input("1/2/3:  "))
pweapon = sweapon_stats[in1-1]
Scenarios.sceneall(pweapon, health,maxhealth, gold)
    	



