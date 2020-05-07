from math import factorial

days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def n_in_factorial_k(n):
    n = str(n)
    k = 0
    while True:
        if n in str(factorial(k)):
            return k
        k += 1

factorial_birthdays = []
for month in range(0, 12):
    for day in range(1, days_in_month[month]+1):
        birthday = "{:02d}{:02d}".format(day, month+1)
        factorial_birthdays.append((birthday, 		
											n_in_factorial_k(birthday)))      
print(sorted(factorial_birthdays, key=lambda x: (x[1], x[0])))
print('-'*30)
print(sorted(factorial_birthdays))
