print("Welcome to Roman Numerals between 1 and 10")
enterLoop = False
while not enterLoop:
    num = int(input("Enter a number between 1 and 10 "))
    if(num == 1):
        print("I")
    elif(num == 2):
        print("II")
    elif(num == 3):
        print("III")
    elif(num == 4):
        print("IV")
    elif(num == 5):
        print("V")
    elif(num == 6):
        print("VI")
    elif(num == 7):
        print("VII")
    elif(num == 8):
        print("VIII")
    elif(num == 9):
        print("IX")
    elif(num == 10):
        print("X")
    else:
        print("Not between 1 and 10")
        break

