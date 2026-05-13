def is_leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

check = is_leap_year(int(input("Input the year : ")))
if check == True:
    print("It is a leap year")
else:
    print("It is not a leap year")

