import random
num1 = random.randint(0, 10)
guessed = False
while(guessed == False):
    num2 = int(input("What's your guess?"))
    if(num2 == num1):
        print("you win!")
        guessed = True
    elif(num2 > num1):
        print("The number is less than your guess")
    elif(num2 < num1):
        print("The number is greater than your guess")
