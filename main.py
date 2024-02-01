import functions
#weapon order (damage, chance of success(%),durability, value )
health = 100
gold = 20
dagger = [10,90,15,10, "Dagger"]
sword =[15,70,12,10, "Sword"]
mace = [20,50,14,10, "Mace"]
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
in1 = input("gd")
functions.user_stats(pweapon, in1, health, gold)





