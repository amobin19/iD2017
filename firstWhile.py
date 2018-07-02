import random
num = random.randint(0, 10)
guessed = False

while not guessed:
    guess = int(input("What is your guess? "))
    if(guess == num):
        print("You are correct!")
        guessed = True;
    elif(guess > num):
        print("Answer is lower than guess. Please try again")
    elif(guess < num):
        print("Answer is higher than guess. Please try again")
    
