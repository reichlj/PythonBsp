import math

n1 = float('nan')
n2 = float('Nan')
n3 = float('NaN')
n4 = float('NAN')

print(n1,n2,n3,n4)

n5 = math.nan
print(n5)
print(math.isnan(n1))

print(n1 == n2)
print(n1 == 0)
print(n1 == 100)
print(n2 < 0)
print(n1 == float('nan'))