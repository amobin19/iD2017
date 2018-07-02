num = int(input("Guessing Number: "))
guess = int(input("Guess?"))

if(num == guess):
    print(guess, "is the right answer!")
elif(num > guess):
    print("Answer is higher")
elif(num < guess):
    print("Answer is lower")
