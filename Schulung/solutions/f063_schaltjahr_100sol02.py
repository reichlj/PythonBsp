year = int(input("Year? "))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            leap_year = True
        else:
            leap_year = False
    else:
        leap_year = True
else:
    leap_year = False

if leap_year:
    print(str(year) + 
            ": leap year!")
else:
    print(str(year) + 
            ": not a leap year!")
