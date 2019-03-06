import random
def dice_roller(d1,d2):
    num_die=d1
    total=0
    if num_die > 0:
        total=total + random.randint(1,d2)
        num_die=num_die-1
    return total

dice_roller(1,20)

1
