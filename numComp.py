bunnies = int(input("Number of Bunnies? "))
snakes = int(input("Number of Snakes? "))
if(bunnies > snakes):
    print("Bunnies are better than snakes!")
elif(snakes > bunnies):
    print("Snakes are better than bunnies!")
elif(snakes == bunnies):
    print("They both equally awesome!")
else:
    print("Not a valid animal!")
