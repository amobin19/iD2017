number = 7
guessed = False
counter = 0
while not guessed and counter <= 5:
    guess = int(input("guess my #: "))
    counter += 1 #counter = counter + 1
    if(guess == number):
        print("correct")
        guessed = True
    else:
        print("try again")
        if(counter == 5):
            print("Game Over. Answer is ", number)
            break
