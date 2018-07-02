import random
loopEnt = False
answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', 'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', 'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', 'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
counter = 0
while not loopEnt and counter < 5:
    q = input("What is your (yes or no) question?")
    num = random.randint(0, 19)
    print(answers[num])
    counter += 1
    if(counter == 1):
        print("You have used",counter,"try.")
    else:
        print("You have used",counter,"tries.")

