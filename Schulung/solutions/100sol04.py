A = 4 * 10 **7
pA = 3.3
B = 7 * 10 ** 7
pB = 1.9

i = 0
while A < B:
	A *= 1 + pA/100.
	B *= 1 + pB/100.
	print('\t' + str(i))
	i += 1 
print(i)
