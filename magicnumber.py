month = int(input("Month: "))
day = int(input("Day: "))
year = int(input("Last 2 digits to year: "))
mult = month * day
if(mult == year):
    print("magic number")
else:
    print("not magic number")
print("The date is", month,"/",day,"/",year)
