input1 = int(input("Main number to guess: "))

#input2 = int(input("Guess: "))
#if input2 != input1:
#    print("The answer is wrong!")
#else:
#    print("The answer is right!")

guessed = False;

while not guessed:
    guess1 = int(input("What's your guess? "))
    if guess1 == input1:
        guessed = True;
        print("You win");
    else:
        print("You lose, try again!")
