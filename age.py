age = int(input("player age: ")) 
if age >= 18:
    print("You could be in college")
elif age >= 13 and age < 18:
    print("You can also attend iD Academies!")
elif age >= 7 and age < 13:
    print("You can attend iD Tech Camps!")
else:
    print("You're young.")
