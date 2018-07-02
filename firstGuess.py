input1 = int(input("Guessing Number: "))
input2 = int(input("What is your guess? "))

if input2 == input1:
    print("The answer is right! The answer is", input1)
else:
    print("The answer is wrong! The answer is", input1)
