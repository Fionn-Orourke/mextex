#functions
def user_stats(pweapon, in1, health,maxhealth, gold):
    if in1 == "stats":
        print("\n",pweapon[4],"\n\tDamage: ",pweapon[0],"\n\tChance of success: ",
               pweapon[1], "\n\tDurability: ", pweapon[2], "\n\tValue: ",pweapon[3],
               "\n\nHealth: ",health, "/", maxhealth,"\nGold: ", gold)
        
def health_func(health, maxhealth, hdif):
    health += hdif
    if health > maxhealth:
        health = maxhealth
    hdif = 0







def action(in1, heal, damg, shop):
    if in1 == "heal":
        health_func()



    


