import random

#Get user inputs
num_die=int(input('How many dice to roll? '))
type_die=int(input('what type of dice to roll? '))
die_mod=int(input('Do you have any modifiers? '))

'''dice_roller function:
       Loops for num_die,
       add a random number between 1 and type_die to total
       add mod_die to total
'''
def dice_roller(die_num,die_type,die_mod):
    num_die=die_num
    total=0
    if num_die > 0:
        total=total + random.randint(1,die_type)
        num_die=num_die-1
    return total + die_mod

#Print the result from calling dice_roller using the user inputs
print(F"You rolled {num_die}d{type_die} + {die_mod}")
print(dice_roller(num_die,type_die,die_mod))
