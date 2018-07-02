import random
 
def random_number(max_int):
    rand = random.randrange(0, max_int)
    return rand
 
a_number = random_number(100)
print(a_number)
