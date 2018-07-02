import random
num = random.randint(0, 10)
guessed = False
while not guessed:
    guess = int(input("What is your guess?"))
    if(guess == num):
        print("You win!")
        guessed = True
    elif(guess < num):
        print("Answer is higher")
    elif(guess > num):
        print("Answer is lower")
