import random
race=("Dragonborn","Dwarf","Elf","GNOME","Half-Elf","Half-Orc","Halfling","Human","Tiefling")
dra_sub=("Black","Blue","Brass","Bronze","Copper","Gold","Green","Red","Silver","White")
dwa_sub=("Hill","Mountain")
elf_sub=("Drow","High","Wood")
gnome_sub=("Deep","Forest","Rock")
halfling_sub=("Lightfoot","Stout")
race_choice=race[random.randint(0,8)]

def sub_race(race):
    if race == "Dragonborn":
        race_full=dra_sub[random.randint(0,9)]+" "+race_choice
    elif race == "Dwarf":
        race_full=dwa_sub[random.randint(0,1)]+" "+race_choice
    elif race == "Elf":
        race_full=elf_sub[random.randint(0,2)]+" "+race_choice
    elif race == "GNOME":
        race_full=gnome_sub[random.randint(0,2)]+" "+race_choice
    elif race == "Halfling":
        race_full=halfling_sub[random.randint(0,2)]+" "+race_choice
    else:
        race_full=race
    return race_full

race_full=sub_race(race_choice)

print("You are a "+ race_full)