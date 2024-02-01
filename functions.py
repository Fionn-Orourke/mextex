#functions
def user_stats(pweapon, in1, health, gold):
    if in1 == "stats":
        print("\n",pweapon[4],"\n\tDamage: ",pweapon[0],"\n\tChance of success: ",
               pweapon[1], "\n\tDurability: ", pweapon[2], "\n\tValue: ",pweapon[3],
               "\n\nHealth: ",health, "\nGold: ", gold)
    


