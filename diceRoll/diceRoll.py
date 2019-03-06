import random 

num_die=int(input('How many dice to roll? '))
type_die=int(input('what type of dice to roll? '))
die_mod=int(input('Do you have any modifiers? '))
total=0
while num_die > 0:
    total=total + random.randint(1,type_die)
    num_die=num_die-1
total=total+die_mod
print(total)
