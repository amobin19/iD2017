print("Welcome to the Python Horoscope Generator!")
month = int(input("Enter the Month You Were Born (ex: 11 for November, 5 for May): "))
day = int(input("Enter the Day You Were Born (ex: 8, 16, 9): "))
if (month == 3 and day >= 21 or month == 4 and day <= 20):
        print("Your sign is Aries")
elif (month == 4 and day >= 21 or month == 5 and day <= 20):
        print("Your sign is Taurus")
elif (month == 5 and day >= 21 or month == 6 and day <= 20):
        print("Your sign is Gemini")
elif (month == 6 and day >= 21 or month == 7 and day <= 22):
        print("Your sign is Cancer")
elif (month == 7 and day >= 23 or month == 8 and day <= 22):
        print("Your sign is Leo")
elif (month == 8 and day >= 23 or month == 9 and day <= 22):
        print("Your sign is Virgo")
elif (month == 9 and day >= 23 or month == 10 and day <= 22):
        print("Your sign is Libra")
elif (month == 10 and day >= 23 or month == 11 and day <= 22):
        print("Your sign is Scorpio")
elif (month == 11 and day >= 23 or month == 12 and day <= 21):
        print("Your sign is Sagittarius")
elif (month == 12 and day >= 21 or month == 1 and day <= 19):
        print("Your sign is Capricorn")
elif (month == 1 and day >= 20 or month == 2 and day <= 19):
        print("Your sign is Aquarius")
elif (month == 2 and day >= 20 or month == 3 and day <= 20):
        print("Your sign is Pisces")
else:
    print("Error, code did not recognize date input")
 
