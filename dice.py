import random
loopEnt = False
answers = [1,2,3,4,5,6]
while not loopEnt:
    question = input("Roll?")
    num = random.randint(0, 5)
    print(answers[num])
