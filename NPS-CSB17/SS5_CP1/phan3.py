# Bai 1
num = float(input("Input a number: "))
if num>13:
    print("This number is larger than 13")
elif num == 13:
    print("It's 13")
else:
    print("This number is not larger than 13")
# Bai 2
num = int(input("Input a number: "))
if num%2==0:
    print("This number is even")
else:
    print("This number is not even")
# Bai 3
month = int(input("Input a month: "))
if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
    print("This month has 31 days")
elif month == 4 or month == 6 or month == 9 or month == 11:
    print("This month has 30 days")
elif month == 2:
    year = int(input("Enter the year: "))

    if year%100==0:
        if year%400==0:
            print("This month has 29 days")
        else:
            print("This month has 28 days")
    elif year%4==0:
        print("This month has 29 days")
    else:
        print("This month has 28 days")
else:
    print("This is not a month?")

