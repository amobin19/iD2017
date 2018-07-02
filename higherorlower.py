import random
print("Welcome to Guessing Game! Please select a range of numbers to guess from.")
minNum = int(input("Select a minimum number: "))
maxNum = int(input("Select a maximum number: "))
input1 = random.randint(minNum, maxNum)
counter = 0;
guessed = False;
while not guessed and counter <= 5:
    print("Guess a number in the range of", minNum, "and", maxNum)
    guess1 = int(input())
    counter += 1
    if(guess1 == input1):
        guessed = True;
        print("You win! You have used", counter, "tries to reach the answer!");
    elif(guess1 > input1 and guess1 <= maxNum):
        print("Value is lower. Try again.")
        if counter == 5:
            print("Too many tries. The answer is", input1)
            break
    elif(guess1 < input1 and guess1 >= minNum):
        print("Value is higher. Try again.")
        if counter == 5:
            print("Too many tries. The answer is", input1)
            break
    elif(guess1 > maxNum or guess1 < minNum):
        print("Out of range. Try again.")
        if counter == 5:
            print("Too many tries. The answer is", input1)
            break
    else:
        print("Not valid input")
        if counter == 5:
            print("Too many tries. The answer is", input1)
            break

#ask for pre-set numbers or manually input min and max
#set difficulties
