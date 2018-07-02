age = int(input("What is your age? "))
if(age <= 0):
    print("Not a valid age")
elif(age >= 1 and age <= 3):
    print("toddler")
elif(age >= 3 and age <= 12):
    print("kid")
elif(age >= 13 and age <= 19):
    print("teen")
elif(age >= 20 and age <= 64):
    print("adult")
elif(age >= 65):
    print("senior")
