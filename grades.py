grade = int(input("grade: "))
if grade == 100:
    print ("You got a perfect score!")
elif grade >= 90 and grade < 100:
    print("You got an A")
elif grade >= 80 and grade < 90:
    print("You got a B")
elif grade >= 70 and grade < 80:
    print("You got a C")
elif grade >= 60 and grade < 70:
    print("You got a D")
elif grade < 60:
    print("You failed.")
else:
    print("You got extra credit!")
