import random
num = random.randint(0, 10)
guessed = False
counter = 0
while not guessed and counter <= 5:
    guess = int(input("Enter a number: "))
    if(num == guess):
        print(guess, "is the right answer!")
        counter += 1
        guessed = True
    elif(num > guess and guess >= 0):
        print("Answer is higher")
        counter += 1
        if(counter == 5):
            print("The right answer is", num)
            break
    elif(num < guess and guess <= 10):
        print("Answer is lower")
        counter += 1
        if(counter == 5):
            print("The right answer is", num)
            break
    else:
        print("number is out of range, please try again")
        counter += 1
        if(counter == 5):
            print("The right answer is", num)
            break

        
        
