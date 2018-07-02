input1 = int(input("Guessing Number: "))
guessed = False;

while not guessed:
    input2 = int(input("Pick a number: "))
    if input2 == input1:
        guessed = True;
        print("That is right! You won!")
    else:
        print("Try Again")
